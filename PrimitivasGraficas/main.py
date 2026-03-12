import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from pygame.locals import *
from sys import exit


# iniciando pygame
pygame.init()

altura = 800
largura = 600

# criação da tela
tela = pygame.display.set_mode((altura, largura), OPENGL | DOUBLEBUF) 

# criação de área desenhável
def init_ortho():
    glMatrixMode(GL_PROJECTION)
    # uma matriz identidade para resetar 
    glLoadIdentity()
    # definir a visão
    gluOrtho2D(0, altura, 0, largura)

init_ortho()

# loop da tela
while True:
    # captura de eventos
    for event in pygame.event.get():
        # verificação de tipos de eventos
        if event.type == QUIT:
            pygame.quit()
            exit(0)

    # inicio de desenho

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # inicio do desenho

    glPointSize(50)
    glBegin(GL_POINTS)
    # inicio do desenho
    glVertex2i(300, 200)
    glEnd()

    # atualização de tela
    pygame.display.flip()