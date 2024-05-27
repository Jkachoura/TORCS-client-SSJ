import glob
import os

import pandas as pd
from pytocl.driver import Driver
from pytocl.car import State, Command

import torch
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np

from pytocl.pytorch_car_model import CarControlModel

MPS_PER_KMH = 1000 / 3600  # Meters per second per kilometer per hour

class MyDriver(Driver):
    # Define RPM thresholds for gear shifting
    RPM_UPSHIFT = 7000
    RPM_DOWNSHIFT = 3000

    def __init__(self, logdata=True):
        super().__init__(logdata)
        latest_scaler_file = max(glob.glob('../models/scaler_*.pkl'), key=os.path.getctime)

        with open(latest_scaler_file, 'rb') as f:
            self.scaler = pickle.load(f)
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = CarControlModel(68, 4).to(self.device)

        latest_model_file = max(glob.glob('../models/model_*.pth'), key=os.path.getctime)
        self.model.load_state_dict(torch.load(latest_model_file))
        self.model.eval()

    def clip(self, v, lo, hi):
        if v < lo:
            return lo
        elif v > hi:
            return hi
        else:
            return v

    def clip_to_limits(self, accel, steer, brake):
        return self.clip(accel, 0, 1), self.clip(brake, 0, 1), self.clip(steer, -1, 1)
    
    def convert_gear_value_back(self, x):
        return (x * 7) - 1

    def transform_car_state(self, carstate: State):
        features = dict()
        features['Angle'] = [(carstate.angle * np.pi) / 180.0] 
        features[' DistanceCovered'] = [carstate.distance_raced]
        # features['lastLapTime'] = [carstate.last_lap_time]
        # TODO remove gear input and maybe output for manual gear shifting logic (Test if it works better without it)
        features[' Gear'] = [carstate.gear]
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
        accel, brake, steer = self.clip_to_limits(prediction[0][0], prediction[0][1], prediction[0][2])
        command.accelerator = accel
        command.steering = steer 
        command.brake = brake

        gear = self.convert_gear_value_back(prediction[0][3])
        command.gear = round(gear)

        # Gear shifting logic for reverse
        if -10 < carstate.speed_x / MPS_PER_KMH < 5 and carstate.distance_raced > 10:
            # If 50% of distance from edge values are <= 0.5
            if len([x for x in carstate.distances_from_edge if x <= 5]) >= 9:
                print("REVERSE")
                print(carstate.distances_from_edge)
                command.gear = -1

        # TODO with this manual gear shifting below enabled the car doesn't drive good
        # Remove gear from the model input and output and check difference in lap finishing time and driving

        # print(carstate.speed_x / MPS_PER_KMH)
        # Gear shifting logic
        # if gear != -1:
        #     if carstate.gear > 0:
        #         if carstate.rpm > self.RPM_UPSHIFT and carstate.gear < 6:
        #             command.gear = carstate.gear + 1
        #         elif carstate.rpm < self.RPM_DOWNSHIFT and carstate.gear > 1:
        #             command.gear = carstate.gear - 1
        #         else:
        #             command.gear = carstate.gear
        #     # else:
        #     #     command.gear = 1  # Start in first gear if neutral or reverse
        # else:
        #     command.gear = gear



        # print(f"Accelerator={accel},{prediction[0][0]:.2f},\tBrake={prediction[0][1]:.2f},\tSteer={prediction[0][2]:.2f},\tgear={gear}")

        if self.data_logger:
            self.data_logger.log(carstate, command)

        return command
