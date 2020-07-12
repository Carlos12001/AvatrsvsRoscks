import pygame

from GameV0 import *

white = (255, 255, 255)
#pos_rook = [type, x, y]
class New_Rook (pygame.sprite.Sprite):
    def __init__(self, tipo,posicion):
        super().__init__()
        self.type_rook = tipo

        self.last_time_atack = 0
        self.last_time_move = 0

        # Rook de arena
        if self.type_rook == 5:
            # cargar imagen
            self.image = pygame.image.load("resource/rook_sand.png").convert()
            self.image.set_colorkey(white)
            self.image = pygame.transform.scale(self.image, (100, 90))
            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]
            self.rect.y = posicion[1]

            # Caracteristicas del sand rook
            self.ps = 7


            self.speed_atack = 4

        # Rook de roca
        elif self.type_rook == 6:
            # cargar imagen
            self.image = pygame.image.load("resource/rook_rock.png").convert()
            self.image.set_colorkey(white)
            self.image = pygame.transform.scale(self.image, (100, 90))
            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]
            self.rect.y = posicion[1]

            # Caracteristicas del sand rook
            self.ps = 14


            self.speed_atack = 6

        # Rook de fuego
        elif self.type_rook == 7:
            # cargar imagen
            self.image = pygame.image.load("resource/rook_fire.png").convert()
            self.image.set_colorkey(white)
            self.image = pygame.transform.scale(self.image, (100, 90))
            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]
            self.rect.y = posicion[1]

            # Caracteristicas del sand rook
            self.ps = 16

            self.speed_atack = 8

        # Rook de agua
        elif self.type_rook == 8:
            # cargar imagen
            self.image = pygame.image.load("resource/rook_water.png").convert()
            self.image.set_colorkey(white)
            self.image = pygame.transform.scale(self.image, (100, 90))
            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]
            self.rect.y = posicion[1]

            # Caracteristicas del sand rook
            self.ps = 16

            self.speed_atack = 10

    # obtener vida
    def ps_get (self):
        return self.ps

    # Obtener imagen
    def image_get(self):
        return self.image

    # Ataque de los Avatrs
    def atack(self, time_now):

        # Revisa el tiempo de ataque
        if (time_now - self.last_time_atack) // 1000 == self.speed_atack:
            self.last_time_atack = time_now

            # Quien realiza el ataque
            if self.type_rook == 5:
                # Logica de cambio de sprite
                atack = Attack_Rook(self.type_rook, self.posicion_get() )

            if self.type_rook == 6:
                # Logica de cambio de sprite
                atack = Attack_Rook(self.type_rook, self.posicion_get() )

            if self.type_rook == 7:
                # Logica de cambio de sprite
                atack = Attack_Rook(self.type_rook, self.posicion_get())

            if self.type_rook == 8:
                # Logica de cambio de sprite
                atack = Attack_Rook(self.type_rook, self.posicion_get())

                pass
            return atack
        else:
            return ('')

    #Obtienes posicion
    def posicion_get(self):
        return [self.rect.x, self.rect.y]

        # Obtener nombre del tipo de enemigo

    def type_get(self):
        if self.type_rook == 5:
            return 'Sand'
        elif self.type_rook == 6:
            return 'Rock'
        elif self.type_rook == 7:
            return 'Fire'
        elif self.type_rook == 8:
            return 'Water'

    # Dibuja el men en pantalla
    def draw_me(self, time_now):
        if self.last_time_move == 0 :
            self.last_time_move = time_now
            self.last_time_atack =  time_now

        screen.blit(self.image, self.posicion_get())


#Atacks
class Attack_Rook (pygame.sprite.Sprite):
    def __init__(self, type, posicion):
        super().__init__()
        self.type = type
        #Arena
        if self.type == 5 :
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (20, 40))

            self.rect = self.image.get_rect()
            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]
            self.rect.y = posicion[1]
            self.pa = 2

            self.speed = 2


        elif self.type == 6 :
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (20, 40))

            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]
            self.rect.y = posicion[1]

            self.pa = 4
            self.speed = 2


        elif self.type == 7 :
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (20, 40))

            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]
            self.rect.y = posicion[1]

            self.pa = 4
            self.speed = 2

        elif self.type == 8 :
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (20, 40))

            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]
            self.rect.y = posicion[1]

            self.pa = 4
            self.speed = 2

    #Trayectoria del ataque
    def trayect( self):
        if self.rect.y<size[1]:
            self.rect.y += self.speed
        else:
            self.kill()


    #Dibujo del ataque
    def dibujar( self):
        screen.blit( self.image, [self.rect.x,self.rect.y] )

    # Obtener ataque
    def pa_get(self):
        return self.pa