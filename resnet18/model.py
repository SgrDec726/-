from torch import nn


class resnet18(nn.Module):
    def __init__(self, num_classes):
        super(resnet18, self).__init__()
        self.features = nn.Sequential()

    def forward(self, x):
        return x