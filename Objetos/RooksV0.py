import pygame
#from GameV0 import *

#Primero funcion crear dibuja en cada cuadrito de la matriz y revisa que no halla ningun personaje en dicho espacio


class New_Rook (pygame.sprite.Sprite):
    def __init__( self, tipo, posicion, num, black, list_config):
        super().__init__()
        self.type_rook = tipo
        self.num = num
        self.last_time_atack = 0

        # Rook de arena
        if self.type_rook == 5:
            # cargar imagen
            self.image = pygame.image.load("resource/rook_sand.png").convert()
            self.image.set_colorkey(black)
            self.image = pygame.transform.scale(self.image, (100, 90))
            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]
            self.rect.y = posicion[1]

            # Caracteristicas del sand rook
            self.ps = 7

            # Velocidad de ataque   OBTENER DEL MENUN DE CONFIG
            self.speed_atack = list_config[4][0]

        # Rook de roca
        elif self.type_rook == 6:
            # cargar imagen
            self.image = pygame.image.load("resource/rook_rock.png").convert()
            self.image.set_colorkey(black)
            self.image = pygame.transform.scale(self.image, (100, 90))
            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]
            self.rect.y = posicion[1]

            # Caracteristicas del sand rook
            self.ps = 14

            # Velocidad de ataque   OBTENER DEL MENUN DE CONFIG
            self.speed_atack = list_config[4][0]

        # Rook de fuego
        elif self.type_rook == 7:
            # cargar imagen
            self.image = pygame.image.load("resource/rook_fire.png").convert()
            self.image.set_colorkey(black)
            self.image = pygame.transform.scale(self.image, (100, 90))
            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]
            self.rect.y = posicion[1]

            # Caracteristicas del sand rook
            self.ps = 16

            # Velocidad de ataque   OBTENER DEL MENUN DE CONFIG
            self.speed_atack = list_config[4][0]

        # Rook de agua
        elif self.type_rook == 8:
            # cargar imagen
            self.image = pygame.image.load("resource/rook_water.png").convert()
            self.image.set_colorkey(black)
            self.image = pygame.transform.scale(self.image, (100, 90))
            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]
            self.rect.y = posicion[1]

            # Caracteristicas del sand rook
            self.ps = 16

            # Velocidad de ataque   OBTENER DEL MENUN DE CONFIG
            self.speed_atack = list_config[4][0]

    # Obtener vida
    def ps_get(self):
        if self.ps <= 0:
            self.kill()
        return self.ps

    # Ataque de los Rooks
    def atack(self, time_now, list_config):
        atack = []
        # Revisa el tiempo de ataque
        if (time_now - self.last_time_atack) // 1000 >= self.speed_atack  and self.ps > 0:
            self.last_time_atack = time_now

            # Quien realiza el ataque
            if self.type_rook == 5:
                # Logica de cambio de sprite
                atack = Attack_Rook(self.type_rook, self.posicion_get(), list_config)

            if self.type_rook == 6:
                # Logica de cambio de sprite
                atack = Attack_Rook(self.type_rook, self.posicion_get(), list_config)

            if self.type_rook == 7:
                # Logica de cambio de sprite
                atack = Attack_Rook(self.type_rook, self.posicion_get(), list_config)

            if self.type_rook == 8:
                # Logica de cambio de sprite
                atack = Attack_Rook(self.type_rook, self.posicion_get(), list_config)

            
            return atack
        elif self.ps<=0:
            self.kill()
            return ''
        else:
            return ('')
     #Obtener imagen

    #Obtienes la imagen
    def image_get(self):
        return self.image
    
    #Obtienes posicion
    def posicion_get(self):
        return [self.rect.x, self.rect.y]

        # Obtener nombre del tipo de enemigo

    #El tipo de rook que es
    def type_get (self) :
        if self.type_rook == 5:
            return 'Sand'
        elif self.type_rook == 6:
            return 'Rock'
        elif self.type_rook == 7:
            return 'Fire'
        elif self.type_rook == 8:
            return 'Water'

    #Funciona como hace la vida
    def life (self, damege) :
        result = ''
        self.ps -= damege

        if self.ps <= 0:
            result = 'i die'
            self.kill()

        else:
            result = 'still a life'

        return result
    
    # Dibuja el men en pantalla
    def draw_me(self, time_now, screen):
        if not self.ps <= 0:
            
            if self.last_time_atack == 0 :
                self.last_time_atack =  time_now

            screen.blit(self.image, self.posicion_get())
        else:
            self.kill()

    #Retorna el identificador del rook
    def who( self ):
        return self.num

    #Metodo que sirve para Cargar todos los estado de guardado
    def set_guardado( self, ps ):
        if ps <= 0:
            self.kill()
        else:
            self.ps = ps

#Atacks
class Attack_Rook (pygame.sprite.Sprite):
    def __init__( self, tipo, posicion, list_config):
        super().__init__()

        self.type = tipo
        self.frame = 0
        #Arena
        if self.type == 5 :
 
            
            # Craracteristicas del pygame
            self.speed = 0.07
            # Caracteristicas del pygame

            self.sheet = pygame.image.load("resource/balas.png")
            self.sheet.set_clip(pygame.Rect(175, 392, 12, 53))
            self.frame = 0
            self.frames_t = 6
            self.states = list_de_frames(175, 392, 12, 53, 12.8, 5)

            #Imagen
            self.image = self.sheet.subsurface(self.sheet.get_clip())



            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]+25
            self.rect.y = posicion[1]

            self.pa = 2
            self.speed = 2

        #Roca
        elif self.type == 6 :

            self.speed = 0.01
            # Caracteristicas del pygame

            self.sheet = pygame.image.load("resource/balas.png")
            self.sheet.set_clip(pygame.Rect( 10, 283, 18, 61 ))
            self.frame = 0
            self.frames_t = 5
            self.states = list_de_frames( 10, 283, 18, 61, 28, 5)

            #Imagen
            self.image = self.sheet.subsurface(self.sheet.get_clip())



            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]+25
            self.rect.y = posicion[1]

            self.pa = 4


            self.speed = 2

        #Fuego
        elif self.type == 7 :

            self.speed = 0.007
            # Caracteristicas del pygame

            self.sheet = pygame.image.load("resource/balas.png")
            self.sheet.set_clip(pygame.Rect( 0, 0, 52, 60 ))
            self.frame = 0
            self.frames_t = 6
            self.states = list_de_frames( 0, 0, 52, 60, 51.8, 5)

            #Imagen
            self.image = self.sheet.subsurface(self.sheet.get_clip())

            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]+25
            self.rect.y = posicion[1]

            self.pa = 8


            self.speed = 2

        #Agua
        elif self.type == 8 :

            # Craracteristicas del pygame
            self.speed = 0.001
            # Caracteristicas del pygame

            self.sheet = pygame.image.load("resource/balas.png")
            self.sheet.set_clip(pygame.Rect( 12, 179, 18, 61 ))
            self.frame = 0
            self.frames_t = 6
            self.states = list_de_frames( 12, 179, 18, 61, 29, 5)

            #Imagen
            self.image = self.sheet.subsurface(self.sheet.get_clip())


            self.rect = self.image.get_rect()
            self.rect.x = posicion[0]+25
            self.rect.y = posicion[1]

            self.pa = 8


            self.speed = 2

    #Trayectoria del ataque
    def update( self, size ):
        if self.rect.y < size[1]:
            self.clip(self.states)
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.rect.y += self.speed
        else:
            self.kill()

    #Dibujo del ataque
    def dibujar( self, screen):
        screen.blit( self.image, [self.rect.x,self.rect.y] )

    #Obtiene el dano e la bala
    def get_damage( self ):
        return self.pa

    #Obtiene el frem a poner
    def get_frame(self, frame_set):
        self.frame += self.speed
        frames = self.frame % self.frames_t
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[int(frames)]

#Escoge el frem
    def clip(self, clipped_rect):
        self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))


#Funciones
def list_de_frames(x1,y1,x2,y2,espacio,frame):
    result  = []
    c= 0
    for frame in range(frame):
        result.append([x1 + espacio * c, y1, x2, y2])
        c+=1

    return result
