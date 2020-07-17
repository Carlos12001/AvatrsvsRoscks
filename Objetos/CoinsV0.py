import pygame,sys,random

class New_Coin (pygame.sprite.Sprite):
    def __init__( self, type_coin, color):
        super().__init__()
        self.type_coin = type_coin
        # Que tipo de moneda

        # Moneda de 25
        if self.type_coin == 1:
            # Caracteristicas del pygame
            Image = pygame.image.load('resource/coin_25.png').convert()
            self.image = pygame.transform.scale(Image, (50, 50))
            self.image.set_colorkey(color)
            self.value = 25
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(200, 800))
            self.rect.y = random.choice(range(10, 750))

        # Moneda de 50
        elif self.type_coin == 2:
            # Caracteristicas del pygame
            Image = pygame.image.load('resource/coin_50.png').convert()
            self.image = pygame.transform.scale(Image, (50, 50))
            self.image.set_colorkey(color)
            self.value = 50
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(200, 800))
            self.rect.y = random.choice(range(10, 750))

        #Leñador
        elif self.type_coin == 3:
            # Caracteristicas del pygame
            Image = pygame.image.load('resource/coin_100.png').convert()
            self.image = pygame.transform.scale(Image, (50, 50))
            self.image.set_colorkey(color)
            self.value = 100
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(200, 800))
            self.rect.y = random.choice(range(10, 750))

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