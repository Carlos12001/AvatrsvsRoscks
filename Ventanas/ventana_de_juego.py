import pygame,sys,random
from GameV0 import *
from Objetos import AvartsV0
# ------------------------------- Pantalla de inicio del menu del juego ------------------------------- #
def juego():


    #Imagen de fondos
    #Por ahorita es el fondo blanco
    #background = pygame.image.load('fondo.png').convert()
    #screen.fill(background,[0,0])


    #Matriz del juego
    matriz_0_dibujo = pygame.image.load('resource/matriz_0.png').convert()




    all_sprites_list =  pygame.sprite.Group ()

    avatar_list = pygame.sprite.Group ()


    level_1 = True
    level_2 = False
    level_3 = False

    #Creacion de Avatars segun el nivel que se encuentra
    if level_1:
        for i in range(51):
            avatar = AvartsV0.New_Avart(random.randint(1,4))

            all_sprites_list.add(avatar)
            avatar_list.add(avatar)

    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
                exit()
        screen.fill(white)
        if level_1:
            screen.blit(matriz_0_dibujo, [250, 0])

            avatar_list.draw(screen)

        clock.tick(60)
        pygame.display.flip()
juego()