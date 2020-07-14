import pygame, sys
from GameV0 import *


global list_config

list_config = []
def text(text, font, color, surface, x, y):
    txtobj = font.render(text, 1, color)
    txtrect = txtobj.get_rect()
    txtrect.center = (x, y)
    surface.blit(txtobj, txtrect)

def read_config():
    global list_config
    ruta = "configuracion.txt"
    file = open(ruta, "r")
    sprite = []
    cont = 0
    for line in file:
        if cont == 2:
            list_config.append(sprite)
            sprite = []
            line = int(line)
            sprite.append(line)
            cont = 1
        else:
            cont += 1
            line = int(line)
            sprite.append(line)
    list_config.append(sprite)


    print(list_config)






# ------------------------------- Pantalla de inicio del menu del juego ------------------------------- #

def menu():
    screen.fill(green) # color de la ventana
    text('Jugar', font, purple, screen, 500, 150)
    text('Configuración', font, purple, screen, 500, 250)
    text('Salon de la fama', font, purple, screen, 500, 350,dark)
    text('Ayuda', font, purple,screen, 500, 450,dark)

    pygame.display.flip()
    run = True
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_button.collidepoint(event.pos):
                    read_config()
                    from Ventanas import ventana_de_juego
                elif config_button.collidepoint(event.pos):
                    from  Ventanas import ventana_config
                elif salon_button.collidepoint(event.pos):
                    # hacer salon de la fama
                    pass
                elif help_button.collidepoint(event.pos):
                    # hacer ayuda
                    pass

        pygame.draw.rect(screen, darkpurple, game_button)
        pygame.draw.rect(screen, darkpurple, config_button)
        pygame.draw.rect(screen, darkpurple, salon_button)
        pygame.draw.rect(screen, darkpurple, help_button)

        text('Jugar', font2, green, screen, game_button.x + 100, game_button.y + 25)
        text('Configuración', font2, green, screen, config_button.x + 100, config_button.y + 25)
        text('Salon de la fama', font2, green, screen, salon_button.x + 100, salon_button.y + 25)
        text('Ayuda', font2, green, screen, help_button.x + 100, help_button.y + 25)

        pygame.display.flip()





menu()
