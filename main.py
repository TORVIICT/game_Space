import pygame, sys
from pygame.locals import *
from random import randint


#VARIABLES GLOBALES
ancho = 900
alto = 480
color=(52,9,60)


class naveEspacial(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave = pygame.image.load('Imagenes/spaceship.png')
        self.naveImage = pygame.transform.scale(self.ImagenNave, (60, 60)) #cambiar de tamaño nave

        self.rect = self.naveImage.get_rect()
        self.rect.centerx = ancho /2
        self.rect.centery = alto - 60

        self.listaDisparo = []
        self.Vida = True

        self.velocidad = 10

    def movimiento(self):
        if self.Vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0 
            elif self.rect.right >= ancho:
                self.rect.right = ancho
            


    def disparar(self):
        pass
    def dibujar(self, superficie):
        superficie.blit(self.naveImage,self.rect)


def SpaceInvader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("SpaceAttak")

    ImagenFondo = pygame.image.load('Imagenes/fondo.jpg')

    jugador = naveEspacial()

    enJuego = True
    while True:
        jugador.movimiento()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if enJuego == True:
                if event.type == pygame.KEYDOWN:
                    if event.key ==K_LEFT:
                        jugador.rect.left -= jugador.velocidad
                    elif event.key == K_RIGHT:
                        jugador.rect.right += jugador.velocidad
                    elif event.key == K_UP:
                        jugador.rect.y -= jugador.velocidad
                    elif event.key == K_DOWN:
                        jugador.rect.y += jugador.velocidad


        ventana.blit(ImagenFondo, (0,0))
        jugador.dibujar(ventana)
        pygame.display.update()

SpaceInvader()

#Movimiento de nave con teclado
        #elif event.type == pygame.KEYDOWN:
                #if event.key ==K_LEFT:
                   # posX -= velocidad
                #elif event.key == K_RIGHT:
                   #posX += velocidad
                #elif event.key == K_UP:
                    #posY -= velocidad
                #elif event.key == K_DOWN:
                    #posY += velocidad

#Movimiento de nave con el mouse
    #posX, posY = pygame.mouse.get_pos()
    #centrar mouse en la imagen
    #posX -= 30
    #posY -= 30



        