import pygame, sys
from GameV0 import *

# --------------------------------------------- Clases ---------------------------------------#

class Entry():
    def __init__ (self, x, y, width, height, text = ""):
        self.rect = pygame

# --------------------------------------------- Funciones ---------------------------------------------- #
# -------------------------------------- Funcion para crear texto -------------------------------------- #

def text(text, font, color, surface, x, y):
    txtobj = font.render(text, 1, color)
    txtrect = txtobj.get_rect()
    txtrect.center = (x, y)
    surface.blit(txtobj, txtrect)


# ---------------------- Ventana dodne el jugador digita su nombre por primera vez --------------------- #

def name():
    screen.fill(dark)  # color la ventana
    text("Ingrese su nombre", font, darkpurple, screen, 505, 105)
    text("Ingrese su nombre", font, green, screen, 500, 100)
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                run = False
                from Ventanas import ventana_de_menu
        # entrada texto del nombre
        # escribir el nombre del jugador en un txt


name()
