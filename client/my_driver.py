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
        with open('./pytocl/models/scaler.pkl', 'rb') as f:
            self.scaler = pickle.load(f)
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = CarControlModel(67, 3).to(self.device)
        self.model.load_state_dict(torch.load('./pytocl/models/model.pth'))
        self.model.eval()

    def clip(self, v, lo, hi):
        if v < lo:
            return lo
        elif v > hi:
            return hi
        else:
            return v

    def clip_to_limits(self, accel, steer, brake):
        print(f"Before clipping: Accelerator={accel:.2f}, Brake={brake:.2f}, Steering={steer:.2f}")
        return self.clip(accel, 0, 1), self.clip(steer, -1, 1), self.clip(brake, 0, 1)

    def transform_car_state(self, carstate: State, scaler):
        features = dict()
        features['Angle'] = [(carstate.angle * np.pi) / 180.0] 
        features[' DistanceCovered'] = [carstate.distance_raced]
        # features['lastLapTime'] = [carstate.last_lap_time]
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
        normalized_features = scaler.transform(features_df)
        tensor_features = torch.tensor(normalized_features, dtype=torch.float32).to(self.device)
        
        # for tensor in tensor_features[0]:
        #     print(tensor)
        return tensor_features

    def predict(self, carstate: State):
        tensor_features = self.transform_car_state(carstate, self.scaler)

        with torch.no_grad():
            prediction = self.model(tensor_features)
        
        return prediction.cpu().numpy()

    def drive(self, carstate: State) -> Command:
        command = Command()
        prediction = self.predict(carstate)
        # accel, brake, steer = prediction[0][0], prediction[0][1], prediction[0][2]
        accel, brake, steer = self.clip_to_limits(prediction[0][0], prediction[0][1], prediction[0][2])
        command.accelerator = accel
        command.steering = steer
        command.brake = brake

        print(f"Accelerator={command.accelerator:.2f}, Brake={command.brake:.2f}, Steering={command.steering:.2f}")

        # self.steer(carstate, 0, command)

        # Gear shifting logic
        if carstate.gear > 0:
            if carstate.rpm > self.RPM_UPSHIFT and carstate.gear < 6:
                command.gear = carstate.gear + 1
            elif carstate.rpm < self.RPM_DOWNSHIFT and carstate.gear > 1:
                command.gear = carstate.gear - 1
            else:
                command.gear = carstate.gear
        else:
            command.gear = 1  # Start in first gear if neutral or reverse

        if self.data_logger:
            self.data_logger.log(carstate, command)

        return command
