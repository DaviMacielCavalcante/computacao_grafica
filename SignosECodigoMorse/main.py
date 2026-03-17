import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from pygame.locals import *
from sys import exit


# iniciando pygame
pygame.init()

altura = 1200
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

stars = [
    (500, 300), 
    (600, 300), 
    (400, 300), 
    (200, 450),
    (200, 150)
]

starts_connections = [
    (stars[0], stars[1]),
    (stars[0], stars[2]),
    (stars[2], stars[3]),
    (stars[2], stars[4])   
]

# Usei o Claude Sonnet 4.6 para fazer o dicionário com base na imagem
morse_name = {
    'D': '-..',
    'A': '.-',
    'V': '...-',
    'I': '..',
    'M': '--',
    'C': '-.-.',
    'E': '.',
    'L': '.-..',
    'N': '-.',
    'T': '-',
}

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

    glPointSize(5)
    glBegin(GL_POINTS)
    for star in stars:
        glVertex2i(*star)
    glEnd()
    
    glBegin(GL_LINES)
    # inicio do desenho
    for star1, star2 in starts_connections:
        glVertex2i(*star1)
        glVertex2i(*star2)
    glEnd()
    
    x = 100
    y = 100 
    
    # inicio do desenho
    for letra in "DAVI MACIEL CAVALCANTE":
        
        if letra == " ":
            x += 30
            continue
        
        for simbolo in morse_name[letra]:
            if simbolo == ".":
                glPointSize(5)
                glBegin(GL_POINTS)
                glVertex2i(x, y)
                glEnd()
            elif simbolo == '-':
                glBegin(GL_LINES)
                glVertex2i(x, y)
                glVertex2i(x + 10, y)
                glEnd()   
            x += 20

    # atualização de tela
    pygame.display.flip()