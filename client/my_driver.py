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
        self.model = CarControlModel().to(self.device)
        self.model.load_state_dict(torch.load('./pytocl/models/car_control_model.pth'))
        self.model.eval()

    def transform_car_state(self, carstate: State, scaler):
        # Extract relevant features from carstate object
        features = {
            'angle': [carstate.angle],
            'rpm': [carstate.rpm],
            'speed_x': [carstate.speed_x / MPS_PER_KMH],
            'speed_y': [carstate.speed_y / MPS_PER_KMH],
            'track_position': [carstate.distance_from_center]
        }

        # Create a DataFrame with the correct feature names
        features_df = pd.DataFrame(features)

        # Normalize features using the scaler
        normalized_features = scaler.transform(features_df)
        
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
        # prediction = self.predict(carstate)
        # command.accelerator = (float(prediction[0][0]) + 1) / 2
        # command.brake = 0.0
        # # command.brake = float(prediction[0][1])
        # command.steering = float(prediction[0][2])
        # # # transform from [-1, 1] to [0, 1]
        # # command.accelerator = (command.accelerator + 1) / 2
        # # # command.accelerator = (command.accelerator + 1) / 2
        # # command.brake = float(prediction[0][1])
        # # command.steering = float(prediction[0][2])

        # # print(f"Predicted: Accelerator={command.accelerator:.2f}, Brake={command.brake:.2f}, Steering={command.steering:.2f}")

        # # Gear shifting logic
        # if carstate.rpm > 8000:
        #     command.gear = carstate.gear + 1
        # elif carstate.rpm < 2500:
        #     command.gear = carstate.gear - 1
        # else:
        #     command.gear = carstate.gear or 1

        # # Ensure gear is within valid range
        # command.gear = max(1, min(6, command.gear))

        # Log data if logger is available
        if self.data_logger:
            self.data_logger.log(carstate, command)

        return command
