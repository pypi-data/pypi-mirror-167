import os
from argparse import ArgumentParser, Namespace
from collections import OrderedDict
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torch.nn import functional as F
from torchsummaryX import summary
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
from fastai.tabular.all import *
import pickle
import os
import pytorch_lightning as pl
from torch.nn import functional as F
from torchsummaryX import summary
import pandas as pd
import torch
import os
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelBinarizer
import pickle
import numpy as np
from torch.nn import functional as F
from torchsummaryX import summary
#matplotlib 패키지 한글 깨짐 처리 시작
import matplotlib.pyplot as plt

#Reshape((1, 28, 28))
#Reshape((28 * 28,))
#Reshape((28 * 28))
class Reshape(torch.nn.Module):
    def __init__(self, shape):
        super().__init__()
        self.shape = shape
        if type(self.shape) == int:
            self.shape = [self.shape]

    def forward(self, x):
        return x.view((-1, *self.shape))
        
#https://en.wikipedia.org/wiki/Dot_product
class DotProduct(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, user_id, movie_id):
        #print(user_id.shape) #torch.Size([1, 1, 100])
        #print(user_id.shape) #torch.Size([1, 1, 100])
        dot_product = (user_id * movie_id).sum(2)
        #print(dot_product.shape) #torch.Size([1, 1])
        return dot_product
        
class RNNLastOutput(torch.nn.Module):
    def __init__(self, input_size=1, hidden_size=32, batch_first=True):
        super().__init__()
        self.rnn = torch.nn.LSTM(input_size=input_size, hidden_size=hidden_size, batch_first=batch_first)
        #self.rnn = torch.nn.GRU(input_size 32, hidden_size=32, batch_first=True)

    def forward(self, x):
        #print(x.shape) #torch.Size([2, 7, 1])
        output, _ = self.rnn(x)
        #print(output.shape) #torch.Size([2, 7, 32])
        x = output[:,-1]
        #print(x.shape) #torch.Size([2, 32])
        return x
