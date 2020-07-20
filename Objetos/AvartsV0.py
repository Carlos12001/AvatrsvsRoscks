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
        #  Tipo de Avatar a crear

        # Arquero
        if self.type_avatar == 1:
            # Caracteristicas del pygame

            self.sheet = pygame.image.load("resource/arque_g.png")
            #self.sheet_atack = pygame.image.load("resource/arch_atack.png")
            self.sheet.set_clip(pygame.Rect(80, 0, 70, 79))
            #self.sheet_atack.set_clip(pygame.Rect(100, 0, 52, 81))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.speed = 0.4
            self.frames_t = 8
            self.frames_at = 10
            self.frame = 0
            self.states = list_de_frames( 80, 0, 70, 79, 256, 8)
            self.states_atack = list_de_frames(100, 73, 52, 81, 360, 10)
            #self.states_atack = [[100, 0, 52, 81], [100 + 360 * 1, 0, 52, 81], [100 + 360 * 2, 0, 52, 81], [100 + 360 * 3, 0, 52, 81], [100 + 360 * 4, 0, 52, 81]
             #                   [100+ 360 * 5, 0, 52, 81], [100+ 360 * 1, 0, 52, 81], [100, 0, 52, 81], [100, 0, 52, 81], [100, 0, 52, 81]]
           

            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()

            self.rect.x = random.choice( range(250, 750, 100))
            self.rect.y = size[1]-100

            #Caracteristicas del arquero
            self.ps = 5

            self.speed_walk = list_config[0][0]
            self.speed_atack = list_config[0][1]

         # Escudero
        elif self.type_avatar == 2:
            # Caracteristicas del pygame
            self.image = pygame.image.load('resource/avatar_escudero.png').convert()
            self.image.set_colorkey(color)
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
            self.image = pygame.image.load('resource/avatar_lenador.png').convert()
            self.image.set_colorkey(color)
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
            self.image = pygame.image.load('resource/avatar_canival.png').convert()
            self.image.set_colorkey(color)
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

    # Obtener imagen
    def image_get(self):
        return self.image

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
            self.clip(self.states_atack )
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            # agregar lineas de clip()
            screen.blit(self.image, self.posicion_get())

        #Cuando ataca solo dibuja el sripite
        elif  self.ps > 0:
            self.clip(self.states_atack)
            self.image = self.sheet.subsurface(self.sheet.get_clip())
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
            
        frames = self.frame % self.frames_t
        
        return frames_list[int(frames)]

    #Animacio_2
    def clip(self, frames_list):
        self.sheet.set_clip(pygame.Rect(self.get_frame(frames_list)))



# Atacks
class Attack_Avatar(pygame.sprite.Sprite):
    def __init__(self, tipo, pos):
        super().__init__()
        self.type = tipo

        # Flechador
        if self.type == 1:
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (20, 40))

            self.rect = self.image.get_rect()

            self.speed = 2
            self.rect.x = pos[0] + 40
            self.rect.y = pos[1]
            self.pa = 2

        # Escuedero
        elif self.type == 2:
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (20, 40))

            self.rect = self.image.get_rect()

            self.speed = 2
            self.rect.x = pos[0] + 40
            self.rect.y = pos[1]
            self.pa = 3

        # Leñador
        elif self.type == 3:
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (1, 1))

            self.rect = self.image.get_rect()

            self.speed = 1
            self.rect.x = pos[0] + 40
            self.rect.y = pos[1]
            self.pa = 9

        # Canival
        elif self.type == 4:
            self.image = pygame.image.load('resource/bala.png').convert()
            self.image = pygame.transform.scale(self.image, (1, 1))

            self.rect = self.image.get_rect()

            self.speed = 1
            self.rect.x = pos[0] + 40
            self.rect.y = pos[1]
            self.pa = 12

    # Hace el trayecto
    def update(self):
        if self.rect.y > -50:
            self.rect.y -= self.speed
        else:
            self.kill()
    
    # Dibuja la bala
    def dibujar(self, screen):
        screen.blit(self.image, [self.rect.x, self.rect.y])
    
    # Obtiene el dano e la bala
    def get_damage(self):
        return self.pa


#Funciones
def list_de_frames(x1,y1,x2,y2,espacio,frame):
    result  = []
    for frame in range(frame):
        result.append([x1 + espacio * frame, y1, x2, y2])

    return result
