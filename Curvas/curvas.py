import pygame
from pygame.locals import *
from sys import exit

# iniciando pygame
pygame.init()

altura = 800
largura = 600

# pontos de controle
p0 = (100, 500)
p1 = (400, 100)
p2 = (700, 500)

def bezier(t):
    
    x = (1 - t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t**2 * p2[0]

    y = (1 - t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t**2 * p2[1]
    return x, y


# criação da tela
tela = pygame.display.set_mode((altura, largura)) 

while True:
    # captura de eventos
    for event in pygame.event.get():
        # verificação de tipos de eventos
        if event.type == QUIT:
            pygame.quit()
            exit(0)

    tela.fill((0,0,0))

    t = 0

    while t <= 1:

        ponto = bezier(t)
        pygame.draw.circle(
            tela, 
            color=(255,255,255),
            center=(int(ponto[0]),int(ponto[1])),
            radius=5
        )

        t += 0.01

    pygame.display.update()