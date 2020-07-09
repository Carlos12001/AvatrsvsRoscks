import pygame,sys,random
from GameV0 import *

#PRimero funcion crear dibuja en cada matriz y revisa que no halla ningun avatar dicha matriz
#Avatars lista mpara saber que tiempo fue puesto cada avatar y para saber cuanto tiempo a pasado el avatar hasta
#Cuando fue puesto y se hace (tiempo actual - tiempo avatar)


class New_Coin (pygame.sprite.Sprite):
    def __init__(self, type_coin):
        super().__init__()

        self.type_coin = type_coin
        #Que tipo de moneda

        # Moneda de 25
        if self.type_coin == 1:
            #Craracteristicas del pygame
            Image = pygame.image.load('resource/coin_25.png').convert()
            self.image = pygame.transform.scale(Image,(50,50))
            self.image.set_colorkey((0,0,0))
            self.value = 25
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(200, 800))
            self.rect.y = random.choice(range(10, 750))

            # Movimiento de moneda
            #self.speedx = random.choice(range(1,5))
            #self.speedy = random.choice(range(1,5))

        # Moneda de 50
        elif self.type_coin == 2:
            # Craracteristicas del pygame
            Image = self.image = pygame.image.load('resource/coin_50.png').convert()
            self.image = pygame.transform.scale(Image, (50, 50))
            self.image.set_colorkey(white)
            self.value = 50
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(200, 800))
            self.rect.y = random.choice(range(10, 750))

            # Movimiento de moneda
            # self.speedx = random.choice(range(1,5))
            # self.speedy = random.choice(range(1,5))

        #Lenador
        elif self.type_coin == 3:
            # Craracteristicas del pygame
            Image = pygame.image.load('resource/coin_100.png').convert()
            self.image = pygame.transform.scale(Image, (50, 50))
            self.image.set_colorkey(white)
            self.value = 100
            self.rect = self.image.get_rect()
            self.rect.x = random.choice(range(200, 800))
            self.rect.y = random.choice(range(10, 750))

            # Movimiento de moneda
            # self.speedx = random.choice(range(1,5))
            # self.speedy = random.choice(range(1,5))

    #def update (self):
        #self.rect.x += self.speedx
        #self.rect.y += self.speedy
        #if self.rect.top > 1000 or self.rect.top <

    #Obtener posicion en X, y
    def posicion_get(self):
        return (self.rect.x,self.rect.y)

    #Obtener nombre del tipo de enemigo
    def type_get(self):
        if self.type_coin == 1:
            return 'Moneda25'
        elif self.type_coin == 2:
            return 'Moneda50'
        elif self.type_coin == 3:
            return 'Moneda100'

    #Obtener imagen
    def image_get(self):
        return self.image

    def value_get(self):
        return self.value

    def draw_me(self):
        screen.blit(self.image, self.posicion_get())