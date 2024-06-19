import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from tqdm.auto import tqdm
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pickle
from datetime import datetime

from carModel import Model
from data_pipeline import load_and_prepare_data, create_dataloaders


def evaluate_in_batches(model, data_loader, device):
    all_preds = []
    all_targets = []
    model.eval()
    with torch.no_grad():
        for inputs, targets in data_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            all_preds.append(outputs.cpu().numpy())
            all_targets.append(targets.cpu().numpy())
    return np.concatenate(all_preds), np.concatenate(all_targets)


def train(epochs, batch_size, learning_rate):
    # Set device to GPU if available
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")

    features, targets, scaler = load_and_prepare_data('new_data')
    train_loader, test_loader, input_size, output_size = create_dataloaders(features, targets, batch_size, device)
    model = Model(input_size, output_size).to(device)
    print(f"Model created with input size: {input_size}, output size: {output_size}")

    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    train_losses = []
    test_losses = []
    train_r2 = []
    test_r2 = []

    for epoch in tqdm(range(epochs)):
        model.train()
        running_loss = 0.0

        for inputs, targets in train_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        epoch_loss = running_loss / len(train_loader)
        train_losses.append(epoch_loss)
        torch.cuda.empty_cache()

        # Evaluation
        train_preds, train_targets = evaluate_in_batches(model, train_loader, device)
        test_preds, test_targets = evaluate_in_batches(model, test_loader, device)

        train_r2_score = r2_score(train_targets, train_preds)
        test_r2_score = r2_score(test_targets, test_preds)

        train_r2.append(train_r2_score)
        test_r2.append(test_r2_score)

        test_preds_tensor = torch.tensor(test_preds, device=device)
        test_targets_tensor = torch.tensor(test_targets, device=device)
        test_loss = criterion(test_preds_tensor, test_targets_tensor).item()
        test_losses.append(test_loss)

        print(f'Epoch {epoch+1}/{epochs}, Train Loss: {epoch_loss}, Test Loss: {test_loss}, Train R2: {train_r2_score}, Test R2: {test_r2_score}')

    return model, scaler, train_losses, test_losses, train_r2, test_r2


def plot_loss_accuracy(train_losses, test_losses, train_r2, test_r2, batch_size, learning_rate):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.plot(train_losses, label='Train')
    ax1.plot(test_losses, label='Test')
    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Loss')
    ax1.legend()

    ax2.plot(train_r2, label='Train')
    ax2.plot(test_r2, label='Test')
    ax2.set_xlabel('Epochs')
    ax2.set_ylabel('Accuracy')
    ax2.legend()

    fig.suptitle(f'Batch Size: {batch_size}, Learning Rate: {learning_rate}')

    fig.savefig(f'graphs/loss_accuracy_{batch_size}_{datetime.now().strftime("%d_%m")}.png')

    return fig


def save_model(model, scaler):
    # Generate timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # Save model with timestamp
    model_path = f'torcs-agent/models/model_{timestamp}.pth'
    torch.save(model.state_dict(), model_path)

    # Save scaler with timestamp
    scaler_path = f'torcs-agent/models/scaler_{timestamp}.pkl'
    with open(scaler_path, 'wb') as f:
        pickle.dump(scaler, f)

    return model_path, scaler_path
