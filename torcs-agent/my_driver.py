import glob
import os
import time

import pandas as pd
from pathlib import Path
from pytocl.driver import Driver
from pytocl.car import State, Command

import torch
import pickle
import numpy as np

from pytocl.pytorch_car_model import CarControlModel

# Global variables
modelFile = 'scaler_*.pkl'
modelFilePath = Path.cwd().joinpath('models').joinpath(modelFile)
MPS_PER_KMH = 1000 / 3600  # Meters per second per kilometer per hour

class MyDriver(Driver):
    # Define RPM thresholds for gear shifting
    RPM_UPSHIFT = 8500
    RPM_DOWNSHIFT = 3000

    def __init__(self, logdata=True):
        super().__init__(logdata)
        latest_scaler_file = max(glob.glob(modelFilePath), key=os.path.getctime)

        with open(latest_scaler_file, 'rb') as f:
            self.scaler = pickle.load(f)
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = CarControlModel(67, 4).to(self.device)

        latest_model_file = max(glob.glob(modelFilePath), key=os.path.getctime)
        self.model.load_state_dict(torch.load(latest_model_file, map_location=self.device))
        self.model.eval()

        self.reverse_start_time = None  # Initialize reverse start time
        self.reverse_duration_limit = 2  # Max duration in reverse in seconds


    def clip(self, v, lo, hi):
        if v < lo:
            return lo
        elif v > hi:
            return hi
        else:
            return v

    def clip_to_limits(self, accel, brake, steer, clutch):
        return self.clip(accel, 0, 1), self.clip(brake, 0, 1), self.clip(steer, -1, 1), self.clip(clutch, 0, 1)
    
    def convert_gear_value_back(self, x):
        return (x * 7) - 1

    def transform_car_state(self, carstate: State):
        features = dict()
        features['Angle'] = [(carstate.angle * np.pi) / 180.0] 
        features[' DistanceCovered'] = [carstate.distance_raced]
        # features['lastLapTime'] = [carstate.last_lap_time]
        # TODO remove gear input and maybe output for manual gear shifting logic (Test if it works better without it)
        # features[' Gear'] = [carstate.gear]
        features[" Opponent_1"] = [carstate.opponents[0]]
        for i in range(1, 36):
            features[f'Opponent_{i+1}'] = [carstate.opponents[i]]
        features[' RPM'] = [carstate.rpm]
        features[' SpeedX'] = [carstate.speed_x / MPS_PER_KMH]
        features[' SpeedY'] = [carstate.speed_y / MPS_PER_KMH]
        features[' SpeedZ'] = [carstate.speed_z / MPS_PER_KMH]
        features[" Track_1"] = [carstate.distances_from_edge[0]]
        for i in range(1, 19):
            features[f'Track_{i+1}'] = [carstate.distances_from_edge[i]]
        features['TrackPosition'] = [carstate.distance_from_center]
        features[" WheelSpinVelocity_1"] = [(carstate.wheel_velocities[0] * np.pi) / 180.0]
        for i in range(1, 4):
            features[f'WheelSpinVelocity_{i+1}'] = [(carstate.wheel_velocities[i] * np.pi) / 180.0]
        features['Z'] = [carstate.z]

        features_df = pd.DataFrame(features)
        normalized_features = self.scaler.transform(features_df)
        tensor_features = torch.tensor(normalized_features, dtype=torch.float32).to(self.device)

        return tensor_features

    def predict(self, carstate: State):
        tensor_features = self.transform_car_state(carstate)

        with torch.no_grad():
            prediction = self.model(tensor_features)
        
        return prediction.cpu().numpy()

    def drive(self, carstate: State) -> Command:
        command = Command()
        prediction = self.predict(carstate)
        accel, brake, steer, clutch = self.clip_to_limits(prediction[0][0], prediction[0][1], prediction[0][2], prediction[0][3])
        command.accelerator = accel
        command.steering = steer 
        command.brake = brake
        command.clutch = clutch

        if carstate.gear != 0:
            if carstate.rpm > self.RPM_UPSHIFT and carstate.gear < 6:
                command.gear = carstate.gear + 1
            elif carstate.rpm < self.RPM_DOWNSHIFT and carstate.gear > 1:
                command.gear = carstate.gear - 1
            else:
                command.gear = carstate.gear
        else:
            command.gear = 1  # Start in first gear if neutral

        if -5 < carstate.speed_x / MPS_PER_KMH < 5 and carstate.distance_raced > 10:
            if len([x for x in carstate.distances_from_edge if x <= 5]) >= 9:
                if self.reverse_start_time is None:
                    self.reverse_start_time = time.time()
                    command.gear = -1
                elif time.time() - self.reverse_start_time <= self.reverse_duration_limit:
                    command.gear = -1
                elif time.time() - self.reverse_start_time <= self.reverse_duration_limit + 4:
                    command.gear = 1
                else:
                    self.reverse_start_time = None

        if self.data_logger:
            self.data_logger.log(carstate, command)

        return command
