import pygame

from GameV0 import *

white = (255, 255, 255)
#pos_rook = [type, x, y]
class Rooks (pygame.sprite.Sprite):
    def __init__(self, pos_rook):
        super().__init__()
        self.type_rook = pos_rook[0]
        self.x = pos_rook[1][0]
        self.y = pos_rook[1][0]

        #if self.type_rook == 5:
        # Rook de arena
        if self.type_rook == 5:
            # cargar imagen
            self.image = pygame.image.load("resource/rook_sand.png").convert()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

            # Caracteristicas del sand rook
            self.ps = 7
            self.pa = 2
            cost_sand = 50

        # Rook de roca
        elif self.type_rook == 6:
            # cargar imagen
            self.image = pygame.image.load("resource/rook_rock.png").convert()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

            # Caracteristicas del sand rook
            self.ps = 14
            self.pa = 4
            cost_rock = 100

        # Rook de fuego
        elif self.type_rook == 7:
            # cargar imagen
            self.image = pygame.image.load("resource/rook_fire.png").convert()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

            # Caracteristicas del sand rook
            self.ps = 16
            self.pa = 8
            cost_fire = 150

        # Rook de agua
        elif self.type_rook == 8:
            # cargar imagen
            self.image = pygame.image.load("resource/rook_water.png").convert()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

            # Caracteristicas del sand rook
            self.ps = 16
            self.pa = 8
            cost_water = 150

    # obtener vida
    def ps_get (self):
        return self.ps

    # obtener ataque
    def pa_get (self):
        return self.pa

    # Obtener imagen
    def image_get(self):
        return self.image

    def position (self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        # primer fila
        if 200 < mouse_pos[0] < 300 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 89:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 250
            self.rect.y = 45
            self.rect = self.image.center((self.rect.x, self.rect.y)) # verificar si esto esta bien
        elif 300 < mouse_pos[0] < 400 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 89:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 350
            self.rect.y = 45
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 400 < mouse_pos[0] < 500 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 89:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 450
            self.rect.y = 45
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 500 < mouse_pos[0] < 600 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 89:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 550
            self.rect.y = 45
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 600 < mouse_pos[0] < 700 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 89:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 650
            self.rect.y = 45
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien

        # segunda fila

        elif 200 < mouse_pos[0] < 300 and mouse_click[0] == 1 and 89 < mouse_pos[1] < 178:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 250
            self.rect.y = 134
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 300 < mouse_pos[0] < 400 and mouse_click[0] == 1 and 89 < mouse_pos[1] < 178:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 350
            self.rect.y = 134
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 400 < mouse_pos[0] < 500 and mouse_click[0] == 1 and 89 < mouse_pos[1] < 178:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 450
            self.rect.y = 134
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 500 < mouse_pos[0] < 600 and mouse_click[0] == 1 and 89 < mouse_pos[1] < 178:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 550
            self.rect.y = 134
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 600 < mouse_pos[0] < 700 and mouse_click[0] == 1 and 89 < mouse_pos[1] < 178:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 650
            self.rect.y = 134
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien

        # tercera fila

        elif 200 < mouse_pos[0] < 300 and mouse_click[0] == 1 and 178 < mouse_pos[1] < 267:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 250
            self.rect.y = 223
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 300 < mouse_pos[0] < 400 and mouse_click[0] == 1 and 178 < mouse_pos[1] < 267:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 350
            self.rect.y = 223
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 400 < mouse_pos[0] < 500 and mouse_click[0] == 1 and 178 < mouse_pos[1] < 267:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 450
            self.rect.y = 223
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 500 < mouse_pos[0] < 600 and mouse_click[0] == 1 and 178 < mouse_pos[1] < 267:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 550
            self.rect.y = 223
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 600 < mouse_pos[0] < 700 and mouse_click[0] == 1 and 178 < mouse_pos[1] < 267:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 650
            self.rect.y = 223
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien

        # cuarta fila

        elif 200 < mouse_pos[0] < 300 and mouse_click[0] == 1 and 267 < mouse_pos[1] < 356:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 250
            self.rect.y = 312
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 300 < mouse_pos[0] < 400 and mouse_click[0] == 1 and 267 < mouse_pos[1] < 356:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 350
            self.rect.y = 312
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 400 < mouse_pos[0] < 500 and mouse_click[0] == 1 and 267 < mouse_pos[1] < 356:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 450
            self.rect.y = 312
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 500 < mouse_pos[0] < 600 and mouse_click[0] == 1 and 267 < mouse_pos[1] < 356:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 550
            self.rect.y = 312
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 600 < mouse_pos[0] < 700 and mouse_click[0] == 1 and 267 < mouse_pos[1] < 356:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 650
            self.rect.y = 312
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien

        # quinta fila

        elif 200 < mouse_pos[0] < 300 and mouse_click[0] == 1 and 356 < mouse_pos[1] < 445:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 250
            self.rect.y = 401
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 300 < mouse_pos[0] < 400 and mouse_click[0] == 1 and 356 < mouse_pos[1] < 445:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 350
            self.rect.y = 401
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 400 < mouse_pos[0] < 500 and mouse_click[0] == 1 and 356 < mouse_pos[1] < 445:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 450
            self.rect.y = 401
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 500 < mouse_pos[0] < 600 and mouse_click[0] == 1 and 356 < mouse_pos[1] < 445:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 550
            self.rect.y = 401
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 600 < mouse_pos[0] < 700 and mouse_click[0] == 1 and 356 < mouse_pos[1] < 445:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 650
            self.rect.y = 401
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien

        # sexta fila

        elif 200 < mouse_pos[0] < 300 and mouse_click[0] == 1 and 455 < mouse_pos[1] < 544:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 250
            self.rect.y = 490
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 300 < mouse_pos[0] < 400 and mouse_click[0] == 1 and 455 < mouse_pos[1] < 544:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 350
            self.rect.y = 490
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 400 < mouse_pos[0] < 500 and mouse_click[0] == 1 and 455 < mouse_pos[1] < 544:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 450
            self.rect.y = 490
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 500 < mouse_pos[0] < 600 and mouse_click[0] == 1 and 455 < mouse_pos[1] < 544:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 550
            self.rect.y = 490
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 600 < mouse_pos[0] < 700 and mouse_click[0] == 1 and 455 < mouse_pos[1] < 544:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 650
            self.rect.y = 490
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien

        # septima fila

        elif 200 < mouse_pos[0] < 300 and mouse_click[0] == 1 and 544 < mouse_pos[1] < 633:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 250
            self.rect.y = 589
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 300 < mouse_pos[0] < 400 and mouse_click[0] == 1 and 544 < mouse_pos[1] < 633:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 350
            self.rect.y = 589
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 400 < mouse_pos[0] < 500 and mouse_click[0] == 1 and 544 < mouse_pos[1] < 633:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 450
            self.rect.y = 589
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 500 < mouse_pos[0] < 600 and mouse_click[0] == 1 and 544 < mouse_pos[1] < 633:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 550
            self.rect.y = 589
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 600 < mouse_pos[0] < 700 and mouse_click[0] == 1 and 544 < mouse_pos[1] < 633:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 650
            self.rect.y = 589
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien

        # octava fila

        elif 200 < mouse_pos[0] < 300 and mouse_click[0] == 1 and 633 < mouse_pos[1] < 722:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 250
            self.rect.y = 678
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 300 < mouse_pos[0] < 400 and mouse_click[0] == 1 and 633 < mouse_pos[1] < 722:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 350
            self.rect.y = 678
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 400 < mouse_pos[0] < 500 and mouse_click[0] == 1 and 633 < mouse_pos[1] < 722:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 450
            self.rect.y = 678
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 500 < mouse_pos[0] < 600 and mouse_click[0] == 1 and 633 < mouse_pos[1] < 722:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 550
            self.rect.y = 678
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 600 < mouse_pos[0] < 700 and mouse_click[0] == 1 and 633 < mouse_pos[1] < 722:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 650
            self.rect.y = 678
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien

        # novena fila

        elif 200 < mouse_pos[0] < 300 and mouse_click[0] == 1 and 722 < mouse_pos[1] < 811:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 250
            self.rect.y = 767
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 300 < mouse_pos[0] < 400 and mouse_click[0] == 1 and 722 < mouse_pos[1] < 811:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 350
            self.rect.y = 767
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 400 < mouse_pos[0] < 500 and mouse_click[0] == 1 and 722 < mouse_pos[1] < 811:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 450
            self.rect.y = 767
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 500 < mouse_pos[0] < 600 and mouse_click[0] == 1 and 722 < mouse_pos[1] < 811:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 550
            self.rect.y = 767
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien
        elif 600 < mouse_pos[0] < 700 and mouse_click[0] == 1 and 722 < mouse_pos[1] < 811:
            # posicionar cada self.type_rook en un a posicion estandar
            self.rect.x = 650
            self.rect.y = 767
            self.rect = self.image.center((rect.x, rect.y))  # verificar si esto esta bien





