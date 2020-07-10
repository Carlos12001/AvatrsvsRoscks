import pygame

from GameV0 import *

white = (255, 255, 255)
#pos_rook = [type, x, y]
class New_Roo (pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()
        self.type_rook = tipo
        #self.x = 0
        #self.y = 0

        #if self.type_rook == 5:
        # Rook de arena
        if self.type_rook == 5:
            # cargar imagen
            self.image = pygame.image.load("resource/rook_sand.png").convert()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
            #self.rect.x = self.x
            #self.rect.y = self.y

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
            #self.rect.x = self.x
            #self.rect.y = self.y

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
            #self.rect.x = self.x
            #self.rect.y = self.y

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
            #self.rect.x = self.x
            #self.rect.y = self.y

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

        # Obtener posicion en X, y
    def posicion_get(self):
        return [self.rect.x, self.rect.y]

        # Obtener nombre del tipo de enemigo
    def type_get(self):
        if self.type_rook == 5:
            return 'Sand'
        elif self.type_rook == 6:
            return 'Rock'
        elif self.type_rook == 7:
            return 'fire'
        elif self.type_rook == 8:
            return 'water'

    def draw_me(self,dontwork):
        screen.blit(self.image, self.posicion_get())

def position (set):
    while set:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        # primer fila
        if 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 90:
            # posicionar cada type_rook en un a posicion estandar
            rectX = 250
            rectY = 0
            set = False
            
        elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 90:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX= 350
            rectY = 0
            set = False
               
        elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 90:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX= 450
            rectY = 0
            set = False
               
        elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 90:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 550
            rectY = 0
            set = False
               
        elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 90:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 650
            rectY = 0
            set = False
               
        # segunda fila

        elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 90 < mouse_pos[1] < 180:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 250
            rectY = 90
            set = False
               
        elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 90 < mouse_pos[1] < 180:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX= 350
            rectY = 90
            set = False
               
        elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 90 < mouse_pos[1] < 180:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX= 450
            rectY = 90
            set = False
               
        elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 90 < mouse_pos[1] < 180:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 550
            rectY = 90
            set = False
               
        elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 90 < mouse_pos[1] < 180:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 650
            rectY = 90
            set = False
               

        # tercera fila

        elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 180 < mouse_pos[1] < 270:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 250
            rectY = 180
            set = False
               
        elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 180 < mouse_pos[1] < 270:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX= 350
            rectY = 180
            set = False
               
        elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 180 < mouse_pos[1] < 270:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX= 450
            rectY = 180
            set = False
               
        elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 180 < mouse_pos[1] < 270:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 550
            rectY = 180
            set = False
               
        elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 180 < mouse_pos[1] < 270:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 650
            rectY = 180
            set = False
               

        # cuarta fila

        elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 270 < mouse_pos[1] < 360:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 250
            rectY = 270
            set = False
            
        elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 270 < mouse_pos[1] < 360:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX  = 350
            rectY = 270
            set = False
            
        elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 270 < mouse_pos[1] < 360:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX  = 450
            rectY = 270
            set = False

        elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 270 < mouse_pos[1] < 360:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX  = 550
            rectY = 270
            set = False

        elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 270 < mouse_pos[1] < 360:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX  = 650
            rectY = 270
            set = False 

        # quinta fila

        elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 360 < mouse_pos[1] < 450:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 250
            rectY = 360
            set = False
     
        elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 360 < mouse_pos[1] < 450:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 350
            rectY = 360
            set = False
            
        elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 360 < mouse_pos[1] < 450:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 450
            rectY = 360
            set = False 

        elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 360 < mouse_pos[1] < 450:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 550
            rectY = 360
            set = False 

        elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 360 < mouse_pos[1] < 450:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 650
            rectY = 360
            set = False 

        # sexta fila

        elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 450 < mouse_pos[1] < 540:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 250
            rectY = 450
            set = False

        elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 450 < mouse_pos[1] < 540:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 350
            rectY = 450
            set = False 

        elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 450 < mouse_pos[1] < 540:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 450
            rectY = 450
            set = False

        elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 450 < mouse_pos[1] < 540:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 550
            rectY = 450
            set = False

        elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 450 < mouse_pos[1] < 540:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 650
            rectY = 450
            set = False   

        # septima fila

        elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 540 < mouse_pos[1] < 630:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 250
            rectY = 540
            set = False  

        elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 540 < mouse_pos[1] < 630:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 350
            rectY = 540
            set = False

        elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 540 < mouse_pos[1] < 630:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 450
            rectY = 540
            set = False
              
        elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 540 < mouse_pos[1] < 630:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 550
            rectY = 540
            set = False  

        elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 540 < mouse_pos[1] < 630:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 650
            rectY = 540
            set = False    

        # octava fila

        elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 630 < mouse_pos[1] < 720:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 250
            rectY = 630
            set = False  
              
        elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 630 < mouse_pos[1] < 720:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 350
            rectY = 630
            set = False 
               
        elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 630 < mouse_pos[1] < 720:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 450
            rectY = 630
            set = False 

        elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 630 < mouse_pos[1] < 720:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 550
            rectY = 630
            set = False 
               
        elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 630 < mouse_pos[1] < 720:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 650
            rectY = 630
            set = False
            
        # novena fila

        elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 720 < mouse_pos[1] < 810:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 250
            rectY = 720
            set = False
            
        elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 720 < mouse_pos[1] < 810:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 350
            rectY = 720
            set = False
               
        elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 720 < mouse_pos[1] < 810:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 450
            rectY = 720
            set = False
            
        elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 720 < mouse_pos[1] < 810:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 550
            rectY = 720
            set = False
              
        elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 720 < mouse_pos[1] < 810:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 650
            rectY = 720
            set = False
    
    return [rectX, rectY]