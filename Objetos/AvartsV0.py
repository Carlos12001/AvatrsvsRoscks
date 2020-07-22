import pygame,sys,random
white = (255, 255, 255)
# Hacer documentacion
#
#
#
class New_Avart (pygame.sprite.Sprite):
    def __init__(self, type_avatar, num, color, size, list_config):
        super().__init__()
        # Tiempo de su creacion
        self.last_time_atack = 0
        self.last_time_move = 0
        self.type_avatar = type_avatar
        self.num = num
        self.atacker = False
        self.frame = 0
        #  Tipo de Avatar a crear

        # Arquero
        if self.type_avatar == 1:

            self.speed = 0.1
            # Caracteristicas del pygame

            self.sheet_1 = pygame.image.load("resource/arque_g.png")
            self.sheet_1.set_clip(pygame.Rect(54, 0, 65, 82))
            self.frames_t = 8
            self.states = list_de_frames( 80, 0, 70, 79, 256, 8)


            self.sheet_2 = pygame.image.load("resource/arque_atack.png")
            self.sheet_2.set_clip(pygame.Rect(95, 0 , 55, 80))
            self.frames_at = 10
            self.states_atack = list_de_frames(95, 0, 55, 80, 360, 10)

            #Imagen
            self.image = self.sheet_1.subsurface(self.sheet_1.get_clip())
            
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()

            self.rect.x = random.choice( range(250, 750, 100))
            self.rect.y = size[1]-100

            #Caracteristicas del arquero
            self.ps = 5

            self.speed_walk = list_config[0][0]
            self.speed_atack = list_config[0][1]

         # Escudero
        
        #Escuedero
        elif self.type_avatar == 2:
            # Caracteristicas del pygame

            #"",  150, 150, , 0.3
            self.speed = 0.1
            # Caracteristicas del pygame

            self.sheet_1 = pygame.image.load("resource/escudero_g.png")
            self.sheet_1.set_clip(pygame.Rect( 55, 0, 63, 79))
            self.frames_t = 15
            self.states = list_de_frames( 55, 0, 63, 79, 154, 15)


            self.sheet_2 = pygame.image.load("resource/escudero_attack.png")
            self.sheet_2.set_clip(pygame.Rect(126, 0 , 66, 87))
            self.frames_at = 22
            self.states_atack = list_de_frames(126, 0, 66, 87, 338.59, 22)

            #Imagen
            self.image = self.sheet_1.subsurface(self.sheet_1.get_clip())
            self.image.set_colorkey(color)
            

            #Posiciones
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(250, 750, 100))
            self.rect.y = size[1] - 100

            # Caracteristicas del escudero
            self.ps = 10

            self.speed_walk = list_config[1][0]
            self.speed_atack = list_config[1][1]

        # Leñador
        elif self.type_avatar == 3:
            # Craracteristicas del pygame
            self.speed = 0.3
            # Caracteristicas del pygame

            self.sheet_1 = pygame.image.load("resource/leñador_ide.png")
            self.sheet_1.set_clip(pygame.Rect(110, 0, 70, 90))
            self.frames_t = 16
            self.states = list_de_frames(110, 0, 70, 90, 311.5, 16)


            self.sheet_2 = pygame.image.load("resource/lenador_attack.png")
            self.sheet_2.set_clip(pygame.Rect(110, 0 , 109, 90)) 
            self.frames_at = 30                                 
            self.states_atack = list_de_frames(110, 0, 109, 90, 312.23, 30)

            #Imagen
            self.image = self.sheet_1.subsurface(self.sheet_1.get_clip())
            self.image.set_colorkey(color)

            #Posiciones
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(250, 750, 100))
            self.rect.y = size[1] - 100

            # Caracteristicas del lenador
            self.ps = 20

            self.speed_walk = list_config[2][0]
            self.speed_atack = list_config[2][1]

        # Canival
        elif self.type_avatar == 4:

            # Craracteristicas del pygame
            self.speed = 0.07
            # Caracteristicas del pygame

            self.sheet_1 = pygame.image.load("resource/canival_g.png")
            self.sheet_1.set_clip(pygame.Rect( 120, 0, 62, 87 ))
            self.frames_t = 6
            self.states = list_de_frames( 120, 0, 62, 87, 171, 6)


            self.sheet_2 = pygame.image.load("resource/canival_attack2.png")
            self.sheet_2.set_clip(pygame.Rect(24, 0 , 159, 86))
            self.frames_at = 6                      #okis okis   
            self.states_atack = list_de_frames(24, 0, 159, 86, 204, 6)
    
            #Imagen
            self.image = self.sheet_1.subsurface(self.sheet_1.get_clip())
            self.image.set_colorkey(color)

            #Posiciones
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(250, 750, 100))
            self.rect.y = size[1] - 100

            # Caracteristicas del canival
            self.ps = 25

            self.speed_walk = list_config[3][0]
            self.speed_atack = list_config[3][1]

    # Obtener posicion en X, y
    def posicion_get(self):
        return [self.rect.x, self.rect.y]

    #Setiadea la posicion
    def posicion_set(self, posicion):
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]

    # Obtener nombre del tipo de enemigo
    def type_get(self):
        if self.type_avatar == 1:
            return 'Arquero'
        elif self.type_avatar == 2:
            return 'Escudero'
        elif self.type_avatar == 3:
            return 'Lenador'
        elif self.type_avatar == 4:
            return 'Canival'

    # Obtener vida
    def ps_get(self):
        if self.ps <= 0:
            self.kill()
        return self.ps

    # Movimiento
    def update(self, time_now):
        if (time_now - self.last_time_move) // 1000 == self.speed_walk and self.ps > 0:
            self.last_time_move = time_now
            self.rect.y -= 90
            return True
        elif self.ps <= 0:
            self.kill()
        else:
            return False

    # Vida
    def life(self, damage):
        result = ''
        self.ps -= damage
        if self.ps <= 0:
            result = 'i die'
        else:
            result = 'still a life'
        return result

    # Ataque de los Avatars
    def atack(self, time_now):
        # Revisa el tiempo de ataque
        if (time_now - self.last_time_atack) // 1000 >= self.speed_atack and self.ps > 0:
            self.last_time_atack = time_now
            self.atacker = True
            self.frame = 0
            # Quien realiza el ataque
            if self.type_avatar == 1:

                atack = Attack_Avatar(self.type_avatar, self.posicion_get())
            if self.type_avatar == 2:

                atack = Attack_Avatar(self.type_avatar, self.posicion_get())
            if self.type_avatar == 3:

                atack = Attack_Avatar(self.type_avatar, self.posicion_get())
            if self.type_avatar == 4:

                atack = Attack_Avatar(self.type_avatar, self.posicion_get())
            return (atack)
        elif self.ps <= 0:
            self.kill()
            return ''
        else:
            return ''

    # Dibuja el men en pantalla
    def draw_me(self, time_now, screen):
        if self.last_time_move == 0:
            self.last_time_move = time_now
            self.last_time_atack = time_now

        #Cuando no ataca se queda animacion inmovil
        if not self.ps <= 0 and not self.atacker:
            self.clip(self.states)

            self.image = self.sheet_1.subsurface(self.sheet_1.get_clip())

            # agregar lineas de clip()
            screen.blit(self.image, self.posicion_get())

        #Cuando ataca solo dibuja el sripite
        elif  self.ps > 0:
            self.clip(self.states_atack)
            self.image = self.sheet_2.subsurface(self.sheet_2.get_clip())



            screen.blit(self.image, self.posicion_get())

        else:
            self.kill()

    # Retorna quien es
    def who(self):
        return self.num

    # Metodo que sirve para Cargar todos los estado de guardado en la Matriz
    def set_guardado(self, posicion, ps):
        if ps <= 0:
            self.kill()
        else:
            self.rect.x = posicion[0]
            self.rect.y = posicion[1]
            self.ps = ps

    #Animacion
    def get_frame(self, frames_list):
        self.frame += self.speed
        if self.frame > (len(frames_list) - 1):
            self.frame = 0
            self.atacker = False

        if not self.atacker:
            frames = self.frame % self.frames_t
        else:
            frames = self.frame % self.frames_at


        return frames_list[int(frames)]

    #Animacio_2
    def clip(self, frames_list):
        #Si esta son atacar
        if not self.atacker:
            self.sheet_1.set_clip(pygame.Rect(self.get_frame(frames_list)))

        #Si esta atacando
        else:
            self.sheet_2.set_clip(pygame.Rect(self.get_frame(frames_list)))



# Atacks
class Attack_Avatar(pygame.sprite.Sprite):
    def __init__(self, tipo, pos):
        super().__init__()
        self.type = tipo

        # Flechador
        if self.type == 1:
            # Craracteristicas del pygame
            self.speed_f = 0.07
            # Caracteristicas del pygame

            self.sheet = pygame.image.load("resource/balas.png")
            self.sheet.set_clip(pygame.Rect(175, 283, 12, 53))
            self.frame = 0
            self.frames_t = 6
            self.states = list_de_frames(175, 283, 12, 53, 12.8, 5)


            #Imagen
            self.image = self.sheet.subsurface(self.sheet.get_clip())

            self.rect = self.image.get_rect()

            self.speed = 2
            self.rect.x = pos[0] + 40
            self.rect.y = pos[1]
            self.pa = 2

        # Escuedero
        elif self.type == 2:
            # Craracteristicas del pygame
            self.speed_f = 0.07
            # Caracteristicas del pygame

            self.sheet = pygame.image.load("resource/shield.png")
            self.sheet.set_clip(pygame.Rect(20, 0, 59, 55))
            self.frame = 0
            self.frames_t = 9
            self.states = list_de_frames(20, 0, 55, 59, 75.33, 9)



            #Imagen
            self.image = self.sheet.subsurface(self.sheet.get_clip())

            self.rect = self.image.get_rect()

            self.speed = 2
            self.rect.x = pos[0] + 40
            self.rect.y = pos[1]
            self.pa = 3

        # Leñador
        elif self.type == 3:
            self.speed_f = 0.07
            # Caracteristicas del pygame

            self.sheet = pygame.image.load("resource/balas.png")
            self.sheet.set_clip(pygame.Rect(175, 283, 12, 53))
            self.frame = 0
            self.frames_t = 6
            self.states = list_de_frames(175, 283, 12, 53, 12.8, 5)

            # Imagen
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            
            self.rect = self.image.get_rect()

            self.speed = 1
            self.rect.x = pos[0] + 40
            self.rect.y = pos[1]
            self.pa = 9

        # Canival
        elif self.type == 4:
            self.speed_f = 0.07
            # Caracteristicas del pygame

            self.sheet = pygame.image.load("resource/balas.png")
            self.sheet.set_clip(pygame.Rect(175, 283, 12, 53))
            self.frame = 0
            self.frames_t = 6
            self.states = list_de_frames(175, 283, 12, 53, 12.8, 5)

            # Imagen
            self.image = self.sheet.subsurface(self.sheet.get_clip())

            self.rect = self.image.get_rect()

            self.speed = 1
            self.rect.x = pos[0] + 40
            self.rect.y = pos[1]
            self.pa = 12

    # Hace el trayecto  y Cambia de animacion
    def update(self):
        if self.rect.y > -50:
            self.clip(self.states)
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.rect.y -= self.speed
        else:
            self.kill()
    
    # Dibuja la bala
    def dibujar(self, screen):
        screen.blit(self.image, [self.rect.x, self.rect.y])
    
    # Obtiene el dano e la bala
    def get_damage(self):
        return self.pa


    def get_frame(self, frame_set):
        self.frame += self.speed_f
        frames = self.frame % self.frames_t
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[int(frames)]

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
