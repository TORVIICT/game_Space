import pygame, sys
from pygame.locals import *
from random import randint



pygame.init()

ventana = pygame.display.set_mode((1400, 900))
pygame.display.set_caption("GAME")

color=(52,9,60)
imagen=pygame.image.load("spaceship.png")
imagen_trans = pygame.transform.scale(imagen, (60, 60)) #cambiar de tamaño nave
#posX = randint(0,300) #ubicacion en X random
posX = 700
posY= 800

velocidad = 10
derecha = True

rectangulo = pygame.Rect(0,0,100,50)





while True:
    ventana.fill(color) #rellena la ventana
    ventana.blit(imagen_trans,(posX,posY))
    pygame.draw.rect(ventana, (180,70,70), rectangulo )

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


#Movimiento de nave con teclado
        #elif event.type == pygame.KEYDOWN:
            if event.key ==K_LEFT:
                posX -= velocidad
            elif event.key == K_RIGHT:
                posX += velocidad
            elif event.key == K_UP:
                posY -= velocidad
            elif event.key == K_DOWN:
                posY += velocidad

#Movimiento de nave con el mouse
    posX, posY = pygame.mouse.get_pos()
    #centrar mouse en la imagen
    posX -= 30
    posY -= 30



    pygame.display.update()