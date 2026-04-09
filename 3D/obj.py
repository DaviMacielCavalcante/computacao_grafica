from math import cos, sin
from pygame.locals import *
from sys import exit
import pygame
import numpy as np

pygame.init()

WINDOW_SIZE = 800
WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

clock = pygame.time.Clock()

# matriz de projeção ortográfica normal
projection_matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

# posição dos vértices
cube_points = [n for n in range(8)]
# posição de xyz (baseados na origem)
cube_points[0] = [[-1], [-1], [1]]
cube_points[1] = [[1], [-1], [1]]
cube_points[2] = [[1], [1], [1]]
cube_points[3] = [[-1], [1], [1]]
cube_points[4] = [[-1], [-1], [-1]]
cube_points[5] = [[1], [-1], [-1]]
cube_points[6] = [[1], [1], [-1]]
cube_points[7] = [[-1], [1], [-1]]

# método de multiplicação de matrizes
def multply_matrix(a, b):
    return (np.array(a) @ np.array(b)).tolist()

angle_x = angle_y = angle_z = 0
scale = 100

while True:
    WINDOW.fill((0, 0, 0))
    # determinação de fps
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # matriz de rotação     
    rotation_x = [
        [1, 0, 0],
        [0, cos(angle_x), -sin(angle_x)],
        [0, sin(angle_x), cos(angle_x)]
    ]    

    rotation_y = [
        [cos(angle_y), 0, sin(angle_y)],
        [0, 1, 0],
        [-sin(angle_y), 0, cos(angle_y)]
    ]

    rotation_z = [
        [cos(angle_z), -sin(angle_z), 0],
        [sin(angle_z), cos(angle_z), 0],
        [0, 0, 1]
    ]

    angle_x += 0.01
    angle_y += 0.01
    angle_z += 0.01

    # desenhando pontos
    for point in cube_points:

        #rotacionando

        rotate_x = multply_matrix(rotation_x, point)
        rotate_y = multply_matrix(rotation_y, rotate_x)
        rotate_z = multply_matrix(rotation_z, rotate_y)

        point2d = multply_matrix(projection_matrix, rotate_z)


        # posicionar os vértices
        x = (point2d[0][0] * scale ) + WINDOW_SIZE/2
        y = (point2d[1][0] * scale ) + WINDOW_SIZE/2

        pygame.draw.circle(surface=WINDOW,color=(255, 0, 0),center=(x, y),radius=5)

    pygame.display.update()