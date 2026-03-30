import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from pygame.locals import *
from sys import exit
from random import random, randint

# iniciando pygame
pygame.init()

altura = 800
largura = 800

# criação da tela
tela = pygame.display.set_mode((largura, altura)) 

# carregando imagem

image = pygame.image.load("imagens/p25f310.png")

bounding = image.get_bounding_rect()

image = image.subsurface(bounding)


# aplicando transformação geométrica

image = pygame.transform.scale(image, (150, 200))

# criação de área desenhável
def init_ortho():
    glMatrixMode(GL_PROJECTION)
    # uma matriz identidade para resetar 
    glLoadIdentity()
    # definir a visão
    gluOrtho2D(0, altura, 0, largura)

#init_ortho()

x = 400
y = 400


angulo = 0

quadro = 0

x_speed = 2
y_speed = 2


# loop da tela
while True:
    # captura de eventos
    for event in pygame.event.get():
        # verificação de tipos de eventos
        if event.type == QUIT:
            pygame.quit()
            exit(0)

        
        while quadro < 200000000:
            # limpar a tela
            tela.fill((0,0,0))

            # fazer ela girar           
            image_rotation = pygame.transform.rotate(image, angle=angulo)
            
            # expor a imagem
            hitbox = image_rotation.get_rect(center=(x,y))
            tela.blit(image_rotation, hitbox)

            angulo += 0.1

            quadro += 10

            if x >= largura:
                x_speed = randint(-2, -1) 
            if x < 0:
                x_speed = randint(1, 2)
            if y < 0:
                y_speed = randint(1, 2)    
            if y >= altura:
                y_speed = randint(-2, -1)
            
            x += x_speed
            y += y_speed            

            pygame.display.flip()

            
            

    # atualização de tela
    pygame.display.flip()