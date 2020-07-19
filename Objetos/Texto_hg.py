import pygame

class Texto_hg_cs(pygame.sprite.Sprite):
    def __init__( self, text, font, color, surface, x , y , num ):

        super().__init__()

        self.num = num
        self.surface = surface
        self.texto_objeto_1 = font.render(text[1], True, color)
        self.texto_pos_1 = self.texto_objeto_1.get_rect()
        self.texto_pos_1.x = x
        self.texto_pos_1.y = y

        self.texto_objeto_2 = font.render(str(text[0])+'s', True, color)
        self.texto_pos_2 = self.texto_objeto_2.get_rect()
        self.texto_pos_2.x = x + 300
        self.texto_pos_2.y = y

        self.texto_objeto_3 = font.render(str(self.num), True, color)
        self.texto_pos_3 = self.texto_objeto_3.get_rect()
        self.texto_pos_3.x = x + 300 + 200
        self.texto_pos_3.y = y


    def update( self , num ):
        self.texto_pos_1.y += num
        self.texto_pos_2.y += num
        self.texto_pos_3.y += num

    def get_num( self ):
        return self.num

    def posicion_get( self ):
        return self.texto_pos_1

    def draw_me( self ):
        self.surface.blit(self.texto_objeto_1, self.texto_pos_1)
        self.surface.blit(self.texto_objeto_2, self.texto_pos_2)
        self.surface.blit(self.texto_objeto_3, self.texto_pos_3)