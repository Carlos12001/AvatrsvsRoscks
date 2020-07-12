import pygame,sys,random
from GameV0 import *

#PRimero funcion crear dibuja en cada matriz y revisa que no halla ningun avatar dicha matriz
#Avatars lista mpara saber que tiempo fue puesto cada avatar y para saber cuanto tiempo a pasado el avatar hasta
#Cuando fue puesto y se hace (tiempo actual - tiempo avatar)


class New_Avart ( pygame.sprite.Sprite ):
    def __init__( self, type_avatar):
        super().__init__()
        #Tiempo de su creacion
        self.last_time_atack  = 0
        self.last_time_move = 0
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


            #carrete de imagenes
            self.image_list = [self.image]

            #Caracteristicas del arquero
            self.ps = 5
            self.pa = 5

            self.speed_walk = 2
            self.speed_atack = 2

        #Escudero
        elif self.type_avatar == 2 :
            # Craracteristicas del pygame
            self.image = pygame.image.load( 'resource/avatar_escudero.png' ).convert()
            self.image.set_colorkey( white )
            self.rect = self.image.get_rect()
            self.rect.x = random.choice( range( 250, 750, 100 ) )
            self.rect.y = size[1] - 100

            # Caracteristicas del escudero
            self.ps = 5
            self.pa = 5

            self.speed_walk = 8
            self.speed_atack = 2

        #Lenador
        elif self.type_avatar == 3 :
            # Craracteristicas del pygame
            self.image = pygame.image.load( 'resource/avatar_lenador.png' ).convert()
            self.image.set_colorkey( white )
            self.rect = self.image.get_rect()
            self.rect.x = random.choice( range( 250, 750, 100 ) )
            self.rect.y = size[1] - 100

            # Caracteristicas del lenador
            self.ps = 5
            self.pa = 5

            self.speed_walk = 14
            self.speed_atack = 2

        #Canival
        elif self.type_avatar == 4:
            # Craracteristicas del pygame
            self.image = pygame.image.load( 'resource/avatar_canival.png' ).convert()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            self.rect.x = random.choice( range( 250, 750, 100 ) )
            self.rect.y = size[1] - 100

            # Caracteristicas del canival
            self.ps = 5
            self.pa = 5

            self.speed_walk = 18
            self.speed_atack = 2

    #Obtener posicion en X, y
    def posicion_get(self):
        return [ self.rect.x, self.rect.y ]

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
    def update(self, time_now):
        if (time_now - self.last_time_move) // 1000 == self.speed_walk:
            self.last_time_move = time_now
            self.rect.y -= 90
            return True
        else:
            return False

    #Ataque de los Avatrs
    def atack(self, time_now):
        #Revisa el tiempo de ataque
        if False: #(time_now - self.last_time_move) // 1000 == self.speed_atack:
            self.last_time_atack = time_now

            #Quien realiza el ataque
            if self.type_avatar == 1:
                #Logica de cambio de sprite
                atack = Attack_Avatar( self.type_avatar, self.posicion_get(), )

            if self.type_avatar == 2:
                # Logica de cambio de sprite
                atack = Attack_Avatar(self.type_avatar, self.posicion_get(), )

            if self.type_avatar == 3:
                # Logica de cambio de sprite
                atack = Attack_Avatar(self.type_avatar, self.posicion_get() )

            if self.type_avatar == 4:
                # Logica de cambio de sprite
                atack = Attack_Avatar(self.type_avatar, self.posicion_get() )

                pass
            return (atack)
        else:
            return ('')

    #Dibuja el men en pantalla
    def draw_me( self, time_now ):
        if self.last_time_move == 0:
            self.last_time_move = time_now
            self.last_time_atack = time_now
        screen.blit(self.image, self.posicion_get())

#Atacks
class Attack_Avatar(pygame.sprite.Sprite):
    def __init__(self, type, pos,rook = None):
        super().__init__()
        self.type = type

        #Flechador
        if self.type == 1:
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (20, 40))

            self.rect = self.image.get_rect()

            self.speed = 2
            self.rect.top = pos(0)
            self.rect.left = pos(1)

        #Escuedero
        elif self.type == 2:
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (20, 40))

            self.rect = self.image.get_rect()

            self.speed = 2
            self.rect.top = pos(0)
            self.rect.left = pos(1)

        #Lenador
        elif self.type == 3:
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (20, 40))

            self.rect = self.image.get_rect()

            self.speed = 2
            self.rect.top = pos(0)
            self.rect.left = pos(1)


        #Canival
        elif self.type == 4:
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (20, 40))

            self.rect = self.image.get_rect()

            self.speed = 2
            self.rect.top = pos(0)
            self.rect.left = pos(1)

    def trayect(self):
        if -50 < self.rect.y < size[1]
            self.rect.top = self.rect.top - self.speed
        else:
            self.kill()

    def dibujar( self):
        screen.blit( self.image, self.rect )


