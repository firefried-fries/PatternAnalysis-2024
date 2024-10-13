"""
Contains source code for training, validating, testing, and saving the model.
Plots losses and metrics during training.
"""
import torch
from modules import *

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
EPOCHS = 300
LEARNING_RATE = 1e-3
BATCH_SIZE = 32
LOG_RESOLUTION = 8  # for 256*256
Z_DIM = 512
W_DIM = 512
LAMBDA_GP = 10


