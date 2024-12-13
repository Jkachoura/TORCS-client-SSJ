import math
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
from torch.utils.data import DataLoader
import os

def load_and_prepare_data(data_folder):
    """
    Load and prepare data for training

    Used CPU for data collection from:
        https://github.com/CognitiaAI/TORCS-Self-Driving-Agent
    """
    # Get list of files in new_data folder
    files = os.listdir(data_folder)

    # Merge all csv files from new_data folder
    df = pd.read_csv(f"new_data/{files[0]}")
    dfs = [pd.read_csv(f'new_data/{file}') for file in files[1:]]
    df = pd.concat(dfs, ignore_index=True)

    # Filter out only the columns we need
    x_columns = [
        "Angle",
        " DistanceCovered",  # Distance raced
        " Opponent_1", "Opponent_2", "Opponent_3", "Opponent_4", "Opponent_5", "Opponent_6", "Opponent_7", "Opponent_8", "Opponent_9", "Opponent_10", "Opponent_11", "Opponent_12", "Opponent_13", "Opponent_14", "Opponent_15", "Opponent_16", "Opponent_17", "Opponent_18", "Opponent_19", "Opponent_20", "Opponent_21", "Opponent_22", "Opponent_23", "Opponent_24", "Opponent_25", "Opponent_26", "Opponent_27", "Opponent_28", "Opponent_29", "Opponent_30", "Opponent_31", "Opponent_32", "Opponent_33", "Opponent_34", "Opponent_35", "Opponent_36",
        " RPM",
        " SpeedX",
        " SpeedY",
        " SpeedZ",
        " Track_1", "Track_2", "Track_3", "Track_4", "Track_5", "Track_6", "Track_7", "Track_8", "Track_9", "Track_10", "Track_11", "Track_12", "Track_13", "Track_14", "Track_15", "Track_16", "Track_17", "Track_18", "Track_19",
        "TrackPosition",
        " WheelSpinVelocity_1",
        "WheelSpinVelocity_2",
        "WheelSpinVelocity_3",
        "WheelSpinVelocity_4",
        "Z",
    ]
    y_columns = [" Acceleration", "Braking", "Steering", "Clutch"]

    # Select relevant columns for features and target
    features = df[x_columns]
    targets = df[y_columns]

    # Normalize features
    scaler = StandardScaler()
    features = scaler.fit_transform(features)

    return features, targets, scaler


def create_dataloaders(features, targets, batch_size, device):
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.2,)

    # Convert to PyTorch tensors
    X_train = torch.tensor(X_train, dtype=torch.float32).to(device)
    X_test = torch.tensor(X_test, dtype=torch.float32).to(device)
    y_train = torch.tensor(y_train.values, dtype=torch.float32).to(device)
    y_test = torch.tensor(y_test.values, dtype=torch.float32).to(device)

    train_dataset = torch.utils.data.TensorDataset(X_train, y_train)
    test_dataset = torch.utils.data.TensorDataset(X_test, y_test)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    input_size = X_train.shape[1]
    output_size = y_train.shape[1]

    return train_loader, test_loader, input_size, output_size