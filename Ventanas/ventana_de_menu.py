import pygame, sys
from GameV0 import *

def text(text, font, color, surface, x, y):
    txtobj = font.render(text, 1, color)
    txtrect = txtobj.get_rect()
    txtrect.center = (x, y)
    surface.blit(txtobj, txtrect)
# ------------------------------- Pantalla de inicio del menu del juego ------------------------------- #

def menu():
    screen.fill(dark) # color de la ventana

    game_button = pygame.Rect(400, 150, 200, 50)
    config_button = pygame.Rect(400, 250, 200, 50)
    salon_button = pygame.Rect(400, 350, 200, 50)
    help_button = pygame.Rect(400, 450, 200, 50)



    pygame.display.flip()
    run = True
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_button.collidepoint(event.pos):
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
