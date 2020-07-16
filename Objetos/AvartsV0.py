import pygame,sys,random
from GameV0 import *

#Primero funcion crear dibuja en cada cuadrito de la matriz y revisa que no halla ningun personaje en dicho espacio



class New_Avart ( pygame.sprite.Sprite ):
    def __init__( self, type_avatar, num ):
        super().__init__()
        #Tiempo de su creacion
        self.last_time_atack  = 0
        self.last_time_move = 0
        self.type_avatar = type_avatar
        self.num = num
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

            self.speed_walk = 2
            self.speed_atack = 5

        #Escudero
        elif self.type_avatar == 2 :
            # Craracteristicas del pygame
            self.image = pygame.image.load( 'resource/avatar_escudero.png' ).convert()
            self.image.set_colorkey( white )
            self.rect = self.image.get_rect()
            self.rect.x = random.choice( range( 250, 750, 100 ) )
            self.rect.y = size[1] - 100

            # Caracteristicas del escudero
            self.ps = 10

            self.speed_walk = 8
            self.speed_atack = 5

        #Lenador
        elif self.type_avatar == 3 :
            # Craracteristicas del pygame
            self.image = pygame.image.load( 'resource/avatar_lenador.png' ).convert()
            self.image.set_colorkey( white )
            self.rect = self.image.get_rect()
            self.rect.x = random.choice( range( 250, 750, 100 ) )
            self.rect.y = size[1] - 100

            # Caracteristicas del lenador
            self.ps = 20

            self.speed_walk = 14
            self.speed_atack = 5

        #Canival
        elif self.type_avatar == 4:
            # Craracteristicas del pygame
            self.image = pygame.image.load( 'resource/avatar_canival.png' ).convert()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            self.rect.x = random.choice( range( 250, 750, 100 ) )
            self.rect.y = size[1] - 100

            # Caracteristicas del canival
            self.ps = 25

            self.speed_walk = 18
            self.speed_atack = 5

    #Obtener posicion en X, y
    def posicion_get( self ):
        return [ self.rect.x, self.rect.y ]

    #Obtener nombre del tipo de enemigo
    def type_get( self ):
        if self.type_avatar == 1:
            return 'Arquero'
        elif self.type_avatar == 2:
            return 'Escudero'
        elif self.type_avatar == 3:
            return 'Lenador'
        elif self.type_avatar == 4:
            return 'Canival'

    #Obtener imagen
    def image_get( self ):
        return self.image

    #Obtener vida
    def ps_get( self ):
        if self.ps <=0:
            self.kill()
        return  self.ps

    #Movimiento
    def update( self, time_now ):
        if (time_now - self.last_time_move) // 1000 == self.speed_walk and self.ps > 0:
            self.last_time_move = time_now
            self.rect.y -= 90
            return True
        elif self.ps <= 0:
            self.kill()
        else:
            return False

    #Vida
    def life( self, damege ):
        result = ''
        self.ps -= damege
        if self.ps <= 0:
            result = 'i die'

        else:
            result = 'still a life'

        return result

    #Ataque de los Avatrs
    def atack( self, time_now ):
        #Revisa el tiempo de ataque
        if (time_now - self.last_time_atack) // 1000 >= self.speed_atack and self.ps>0:
            self.last_time_atack = time_now
            #Quien realiza el ataque
            if self.type_avatar == 1:
                #Logica de cambio de sprite
                atack = Attack_Avatar( self.type_avatar, self.posicion_get() ) 

            if self.type_avatar == 2:
                # Logica de cambio de sprite
                atack = Attack_Avatar(self.type_avatar, self.posicion_get() )

            if self.type_avatar == 3:
                # Logica de cambio de sprite
                atack = Attack_Avatar(self.type_avatar, self.posicion_get() )

            if self.type_avatar == 4:
                # Logica de cambio de sprite
                atack = Attack_Avatar(self.type_avatar, self.posicion_get())

               
            return (atack)
        elif self.ps<=0:
            self.kill()
            return ''
        else:
            return ('')

    #Dibuja el men en pantalla
    def draw_me( self, time_now ):
        if self.last_time_move == 0 :
            self.last_time_move = time_now
            self.last_time_atack = time_now

        if not self.ps<=0:
            screen.blit(self.image, self.posicion_get())
        else:
            self.kill()

    #Retorna quien es
    def who( self ):
        return self.num

    #Metodo que sirve para Cargar todos los estado de guardado
    def set_guardado( self, posicion, ps ):
        if ps <= 0:
            self.kill()
        else:
            self.posicion.x = posicion[0]
            self.posicion.y = posicion[1]
            self.ps = ps

        

#Atacks
class Attack_Avatar(pygame.sprite.Sprite):
    def __init__(self, tipo, pos):
        super().__init__()
        self.type = tipo

        #Flechador
        if self.type == 1:
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (20, 40))

            self.rect = self.image.get_rect()

            self.speed = 2
            self.rect.x = pos[0]+40
            self.rect.y = pos[1]
            self.pa = 2

        #Escuedero
        elif self.type == 2:
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (20, 40))

            self.rect = self.image.get_rect()

            self.speed = 2
            self.rect.x = pos[0]+40
            self.rect.y = pos[1]
            self.pa = 3

        #Lenador
        elif self.type == 3 :
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (1, 1))



            self.rect = self.image.get_rect()

            self.speed = 1
            self.rect.x = pos[0]+40
            self.rect.y = pos[1]
            self.pa = 9


        #Canival
        elif self.type == 4 :
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (1, 1))

            self.rect = self.image.get_rect()

            self.speed = 1
            self.rect.x = pos[0]+40
            self.rect.y = pos[1]
            self.pa = 12

    #Hace el trayecto
    def update(self):
        if self.rect.y > -50:
            self.rect.y -= self.speed
        else:
            self.kill()
    
    #Dibuja la bala
    def dibujar( self ):
        screen.blit( self.image, [self.rect.x,self.rect.y])
    
    #Obtiene el dano e la bala
    def get_damage(self):
        return self.pa

