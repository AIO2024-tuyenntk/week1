import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        return torch.exp(x) / torch.sum(torch.exp(x), dim=0, keepdim=True)
