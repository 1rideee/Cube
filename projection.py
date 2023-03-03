import pygame
import numpy as np
import math
import rotations

WHITE = (255, 255, 255)

RED = (255, 0, 0)

BLACK = (0,0,0)

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Title ")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 100


angle = 0.1

circle_pos = [WIDTH/2 ,HEIGHT/2]


def rotate_x(angle): 
    return np.array([[ 1, 0, 0],
    [0, np.cos(angle), -np.sin(angle)],
    [0, np.sin(angle), np.cos(angle)]])

def rotate_y(angle): 
    return np.array([[ np.cos(angle), 0, np.sin(angle)],
    [0, 1, 0],
    [-np.sin(angle), 0, np.cos(angle)]])

def rotate_z(angle): 
    return np.array([[ np.cos(angle), -np.sin(angle), 0],
    [np.sin(angle), np.cos(angle), 0],
    [0, 0, 1]])

points = np.array([[-1,-1, 1],[1,-1,1],[1,1,1],[-1,1,1],[-1,-1,1],[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1]])

projection_matrix = np.array([[1,0,0],[0,1,0],[0,0,0]])

projected_points= [[n,n] for n in range(len(points))]


def Connect_lines(i,j, points):
    pygame.draw.line(screen, BLACK, (points[i][0], points[i][1]),(points[j][0], points[j][1]))

FPS = pygame.time.Clock()
while True:

    FPS.tick(60)
    angle +=0.01
    
    screen.fill(WHITE)
    i = 0
    for point in points:
        rotate = np.dot(rotate_y(angle), point.reshape((3,1)))
        rotate = np.dot(rotate_z(angle), rotate)
         
        projected2d = np.dot(projection_matrix, rotate)


        x = int(projected2d[0][0]*scale) + circle_pos[0]
        y = int(projected2d[1][0]*scale) + circle_pos[1]
        
        projected_points[i]=[x, y]
        pygame.draw.circle(screen, BLACK, (x,y), 5)
        i+=1
    
    
        Connect_lines(0,1, projected_points)

    pygame.display.update()