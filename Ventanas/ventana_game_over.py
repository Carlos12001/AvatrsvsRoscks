import pygame, sys
from GameV0 import *
#from Ventanas import ventana_nuevo_nombre
#global player_name
#player_name = ventana_nuevo_nombre.user_name

def game_over_ani():


    again = pygame.Rect(380, 650, 220, 50)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if again.collidepoint(event.pos):
                    import GameV0
                    start()

        screen.fill(dark)  # color la ventana
        pygame.draw.rect(screen, brown, again)
        text("Game Over", font, darkpurple, screen, 505, 105)


        pygame.display.flip()

game_over_ani()