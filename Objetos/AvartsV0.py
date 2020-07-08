import pygame,sys,random
from GameV0 import *

#PRimero funcion crear dibuja en cada matriz y revisa que no halla ningun avatar dicha matriz
#Avatars lista mpara saber que tiempo fue puesto cada avatar y para saber cuanto tiempo a pasado el avatar hasta
#Cuando fue puesto y se hace (tiempo actual - tiempo avatar)


class New_Avart ( pygame.sprite.Sprite ):
    def __init__( self, type_avatar ):
        super().__init__()

        self.type_avatar = type_avatar
        #Que tipo de Avatar va crear

        #Arquero
        if self.type_avatar == 1 :
            #Craracteristicas del pygame
            self.image = pygame.image.load( 'resource/avatar_flechador.png' ).convert()
            self.image.set_colorkey( white )
            self.rect = self.image.get_rect()
            self.rect.x = random.choice( range( 250, 750 ,100 ) )
            self.rect.y = size[1]-100

            #Caracteristicas del arquero
            self.ps = 5
            self.pa = 5

            self.speed_walk = 2
            self.speed_atack = 1.25

        #Escudero
        elif self.type_avatar == 2 :
            # Craracteristicas del pygame
            self.image = pygame.image.load('resource/avatar_escudero.png').convert()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(250, 750, 100))
            self.rect.y = size[1] - 100

            # Caracteristicas del escudero
            self.ps = 5
            self.pa = 5

            self.speed_walk = 2
            self.speed_atack = 1.25

        #Lenador
        elif self.type_avatar == 3 :
            # Craracteristicas del pygame
            self.image = pygame.image.load('resource/avatar_lenador.png').convert()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(250, 750, 100))
            self.rect.y = size[1] - 100

            # Caracteristicas del lenador
            self.ps = 5
            self.pa = 5

            self.speed_walk = 2
            self.speed_atack = 1.25

        #Canival
        elif self.type_avatar == 4:
            # Craracteristicas del pygame
            self.image = pygame.image.load('resource/avatar_canival.png').convert()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(250, 750, 100))
            self.rect.y = size[1] - 100

            # Caracteristicas del canival
            self.ps = 5
            self.pa = 5

            self.speed_walk = 2
            self.speed_atack = 1.25

    #Obtener posicion en X, y
    def posicion_get(self):
        return (self.rect.x,self.rect.y)

    #Obtener nombre del tipo de enemigo
    def type_get(self):
        if self.type_avatar == 1:
            return 'Arquero'
        elif self.type_avatar == 2:
            return 'Escudero'
        elif self.type_avatar == 3:
            return 'Lenador'
        elif self.type_avatar == 4:
            return 'Canival'

    #Obtener imagen
    def image_get(self):
        return self.image
    #Movimiento
    def update(self):
        self.rect.y -= 100
