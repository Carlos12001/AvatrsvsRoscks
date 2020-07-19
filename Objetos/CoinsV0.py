import pygame,sys,random

class New_Coin (pygame.sprite.Sprite):
    def __init__( self, type_coin, color):
        super().__init__()
        self.type_coin = type_coin
        # Que tipo de moneda

        # Moneda de 25
        if self.type_coin == 1:
            # Caracteristicas del pygame
            self.sheet = pygame.image.load('resource/coin_copper.png').convert()
            self.sheet.set_colorkey(color)
            self.sheet.set_clip(pygame.Rect(0, 0, 64, 64))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(350, 650))
            self.rect.y = random.choice(range(10, 750))
            self.rect.center = self.rect.x, self.rect.y
            self.frame = 0
            self.states = [[0, 0, 64, 64], [64, 0, 64, 64], [128, 0, 64, 64], [192, 0, 64, 64],
                           [256, 0, 64, 64], [320, 0, 64, 64], [384, 0, 64, 64], [448, 0, 64, 64]]
            self.value = 25

        # Moneda de 50
        elif self.type_coin == 2:
            # Caracteristicas del pygame
            self.sheet = pygame.image.load('resource/coin_silver.png').convert()
            self.sheet.set_colorkey(color)
            self.sheet.set_clip(pygame.Rect(0, 0, 64, 64))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(350, 650))
            self.rect.y = random.choice(range(10, 750))
            self.rect.center = self.rect.x, self.rect.y
            self.frame = 0
            self.states = [[0, 0, 64, 64], [64, 0, 64, 64], [128, 0, 64, 64], [192, 0, 64, 64],
                           [256, 0, 64, 64], [320, 0, 64, 64], [384, 0, 64, 64], [448, 0, 64, 64]]
            self.value = 50

        #Leñador
        elif self.type_coin == 3:
            # Caracteristicas del pygame
            self.sheet = pygame.image.load('resource/coin_gold.png').convert()
            self.sheet.set_colorkey(color)
            self.sheet.set_clip(pygame.Rect(0, 0, 64, 64))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(350, 650))
            self.rect.y = random.choice(range(10, 750))
            self.rect.center = self.rect.x, self.rect.y
            self.frame = 0
            self.states = [[0, 0, 64, 64], [64, 0, 64, 64], [128, 0, 64, 64], [192, 0, 64, 64],
                           [256, 0, 64, 64], [320, 0, 64, 64], [384, 0, 64, 64], [448, 0, 64, 64]]
            self.value = 100

    def get_frame(self, frame_set):
        self.frame += 0.2
        frames = self.frame % 8
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[int(frames)]

    def clip(self, clipped_rect):
        self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))


    def update(self, screen):
        self.clip(self.states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        screen.blit(self.image, self.rect)

    # Obtener posicion en X, y
    def posicion_get(self):
        return [self.rect.x, self.rect.y]

    # Obtener nombre del tipo de moneda
    def type_get(self):
        if self.type_coin == 1:
            return 'Moneda25'
        elif self.type_coin == 2:
            return 'Moneda50'
        elif self.type_coin == 3:
            return 'Moneda100'

    #Obtener imagen
    #def image_get(self):
     #   return self.image

    # Obtener valor
    def value_get(self):
        return self.value

    # Dibujar en pantalla
    def draw_me(self, screen):
        screen.blit(self.image, self.posicion_get())

