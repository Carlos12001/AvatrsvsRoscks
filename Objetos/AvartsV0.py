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
        #  Tipo de Avatar a crear

        # Arquero
        if self.type_avatar == 1:
            # Caracteristicas del pygame

            # 256, 256, 8, 0.2
            self.sheet = pygame.image.load("resource/arque_g.png")
            self.sheet.set_clip(pygame.Rect(80, 0, 70, 79))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.speed = 0.2
            self.frames_t = 8
            self.frame = 0
            self.states = []

            for frame in range(self.frames_t):
                self.states.append([256 * self.frame, 0, 256, 256])






            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()

            self.rect.x = 450#random.choice( range(250, 750, 100))
            self.rect.y = size[1]-100

            # Carrete de imagenes
            self.image_list = [self.image]

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
            # Quien realiza el ataque
            if self.type_avatar == 1:
                # Logica de cambio de sprite
                atack = Attack_Avatar(self.type_avatar, self.posicion_get())
            if self.type_avatar == 2:
                # Logica de cambio de sprite
                atack = Attack_Avatar(self.type_avatar, self.posicion_get())
            if self.type_avatar == 3:
                # Logica de cambio de sprite
                atack = Attack_Avatar(self.type_avatar, self.posicion_get())
            if self.type_avatar == 4:
                # Logica de cambio de sprite
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

        if not self.ps <= 0 and self.type_avatar == 1:
            self.clip(self.states)
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            # agregar lineas de clip()
            screen.blit(self.image, self.posicion_get())

        elif not self.ps <= 0:
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

   # def get_frame(self, frame_set):
        #self.frame += self.speed
        #frames = self.frame % self.frames_t
        #if self.frame > (len(frame_set) - 1):
            self.frame = 0
        #return frame_set[int(frames)]

    def clip(self, clipped_rect):
        self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))



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

