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
    def __init__(self, logdata=True):
        super().__init__(logdata)

        # Load scaler
        with open('./pytocl/models/scaler.pkl', 'rb') as f:
            self.scaler = pickle.load(f)
        
        # Load model and move to GPU if available
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = CarControlModel(68, 3).to(self.device)
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
        """There pretty much is never a reason to send the server
        something like (steer 9483.323). This comes up all the time
        and it's probably just more sensible to always clip it than to
        worry about when to. The "clip" command is still a snakeoil
        utility function, but it should be used only for non standard
        things or non obvious limits (limit the steering to the left,
        for example). For normal limits, simply don't worry about it."""
        # print(f"Before clipping: Accelerator={accel:.2f}, Brake={brake:.2f}, Steering={steer:.2f}")
        return self.clip(accel, 0, 1), self.clip(steer, -1, 1) * -1, self.clip(brake, 0, 1)

    def transform_car_state(self, carstate: State, scaler):
        # Extract relevant features from carstate object
        features = dict()
        features['angle'] = [(carstate.angle * np.pi) / 180.0] # Convert to radian
        features['distRaced'] = [carstate.distance_raced]
        features['lastLapTime'] = [carstate.last_lap_time]
        for i in range(36):
            features[f'opponent{i+1}'] = [carstate.opponents[i]]
        features['rpm'] = [carstate.rpm]
        features['speedX'] = [carstate.speed_x / MPS_PER_KMH]
        features['speedY'] = [carstate.speed_y / MPS_PER_KMH]
        features['speedZ'] = [carstate.speed_z / MPS_PER_KMH]
        for i in range(19):
            features[f'track{i+1}'] = [carstate.distances_from_edge[i]]
        features['trackPos'] = [carstate.distance_from_center]
        for i in range(4):
            features[f'wheelSpinVel{i+1}'] = [(carstate.wheel_velocities[i] * np.pi) / 180.0]
        features['z'] = [carstate.z]


        # Create a DataFrame with the correct feature names
        features_df = pd.DataFrame(features)

        # Normalize features using the scaler
        normalized_features = scaler.transform(features_df)
        for key in features:
            print(f"{key}: {features[key]}")
        
        # Convert to PyTorch tensor and move to GPU if available
        tensor_features = torch.tensor(normalized_features, dtype=torch.float32).to(self.device)
        
        return tensor_features

    def predict(self, carstate: State):
        tensor_features = self.transform_car_state(carstate, self.scaler)

        with torch.no_grad():
            prediction = self.model(tensor_features)
        
        return prediction.cpu().numpy()  # Convert prediction to NumPy array

    def drive(self, carstate: State) -> Command:
        command = Command()

        # command.accelerator = 99999

        # Get model predictions
        prediction = self.predict(carstate)
        accel, steer, brake = self.clip_to_limits(prediction[0][0], prediction[0][1], prediction[0][2])
        command.accelerator = accel
        command.steering = steer
        command.brake = brake
        # command.accelerator = (float(prediction[0][0]) + 1) / 2
        # command.brake = 0.0
        # # command.brake = float(prediction[0][1])
        # command.steering = float(prediction[0][2])
        # # # transform from [-1, 1] to [0, 1]
        # # command.accelerator = (command.accelerator + 1) / 2
        # # # command.accelerator = (command.accelerator + 1) / 2
        # # command.brake = float(prediction[0][1])
        # # command.steering = float(prediction[0][2])

        # gear = carstate.gear
        # rpm = carstate.rpm
        # # logic for reverse start
        # if rpm >= 9200 and gear < 6:
        #     command.gear += 1
        # elif rpm <= 5500 and gear > 1:
        #     command.gear -= 1

        print(f"Predicted: Accelerator={command.accelerator:.2f}, Brake={command.brake:.2f}, Steering={command.steering:.2f}")

        # Gear shifting logic
        # if carstate.rpm > 8000:
        #     command.gear = carstate.gear + 1
        # elif carstate.rpm < 2500:
        #     command.gear = carstate.gear - 1
        # else:
        #     command.gear = carstate.gear or 1
        command.gear = 1
        # command.brake = 0


        # # Ensure gear is within valid range
        # command.gear = max(1, min(6, command.gear))

        # Log data if logger is available
        if self.data_logger:
            self.data_logger.log(carstate, command)

        return command
