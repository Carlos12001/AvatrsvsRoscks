import pygame,sys
from GameV0 import *
# ------------------------------- Pantalla de inicio del menu del juego ------------------------------- #
def juego():

    #Imagen de fondos
    #Por ahorita es el fondo blanco
    #background = pygame.image.load('fondo.png').convert()
    #screen.fill(background,[0,0])


    #Matriz del juego
    matriz_0 = pygame.image.load('resource/matriz_0.png').convert()



    game_over=False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
                exit()
        screen.fill(white)
        screen.blit(matriz_0, [250, 0])
        pygame.display.flip()
juego()