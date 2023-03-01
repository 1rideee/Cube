import pygame as pg
import numpy as np


class RubiksCube:
    def __init__(self, render) :
        self.render = render
        self.vertexes = np.array([(0,0,0,1),(0,1,0,1), (1) ])
    
        self.faces = np.array()