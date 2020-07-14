import pygame, sys
from GameV0 import *
# ------------------------------- Pantalla de inicio del menu del juego ------------------------------- #

def menu():
    screen.fill(green) # color de la ventana
    text('Jugar', font, purple, screen, 500, 150,dark)
    text('Configuración', font, purple, screen, 500, 250,dark)
    text('Salon de la fama', font, purple, screen, 500, 350,dark)
    text('Ayuda', font, purple,screen, 500, 450,dark)

    pygame.display.flip()
    run = True
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()


        #Verificar si presiona algun cartel
        if 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 125< mouse_pos[1] < 175:
            from Ventanas import ventana_de_juego



        pygame.display.flip()





menu()
