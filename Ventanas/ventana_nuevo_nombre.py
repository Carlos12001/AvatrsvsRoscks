import pygame, sys
from GameV0 import *

# --------------------------------------------- Clases ---------------------------------------#

# --------------------------------------------- Funciones ---------------------------------------------- #
# -------------------------------------- Funcion para crear texto -------------------------------------- #

def text(text, font, color, surface, x, y):
    txtobj = font.render(text, 1, color)
    txtrect = txtobj.get_rect()
    txtrect.center = (x, y)
    surface.blit(txtobj, txtrect)


# ---------------------- Ventana dodne el jugador digita su nombre por primera vez --------------------- #


def name():
    entrybox = pygame.Rect(400,300,200,50)
    button = pygame.Rect(440, 400, 140, 50)
    user_name = ""
    active = False
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if entrybox.collidepoint(event.pos):
                    active = True
                elif button.collidepoint(event.pos) and user_name != "":
                    # agregar la escritura del nombre 
                    run = False
                    from Ventanas import ventana_de_menu
                else:
                    active = False

            elif event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_name = user_name [0:-1]
                    elif event.key == pygame.K_TAB:
                        user_name = user_name
                    #elif event.key == pygame.K_
                    else:
                        user_name += event.unicode

                #from Ventanas import ventana_de_menu
                #run = False
        screen.fill(dark)  # color la ventana
        pygame.draw.rect(screen, brown,entrybox)
        pygame.draw.rect(screen, green, button)
        text("Ingrese su nombre", font, darkpurple, screen, 505, 105)
        text("Ingrese su nombre", font, green, screen, 500, 100)
        text(user_name, font2, white,screen, entrybox.x + 100, entrybox.y + 25)
        text("Guardar", font2, dark, screen, button.x + 70, button.y + 25)


        pygame.display.flip()




        # entrada texto del nombre
        # escribir el nombre del jugador en un txt


name()
