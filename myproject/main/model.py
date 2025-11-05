import torch
import torch.nn as nn

class SeqSimplifier(nn.Module):
    def __init__(self, input_size=89, hidden=256, layers=2):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden, layers, batch_first=True)
        self.fc = nn.Linear(hidden, 88)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        y, _ = self.lstm(x)
        return self.sigmoid(self.fc(y))
