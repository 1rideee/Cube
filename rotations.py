
import numpy as np



def rotate_z(angle):
    return np.array([
    [np.cos(angle), -np.sin(angle), 0]
    [np.sin(angle), np.cos(angle), 0],
    [0, 0, 1]])