import pygame,sys,random
from GameV0 import *
from Objetos import AvartsV0


#Matriz de posiciones de juego
global MATRIZ, all_sprites_matriz_list
MATRIZ = [    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [250, 0]],    ['Vacio', [350, 0]],   ['Vacio', [450, 0]],    ['Vacio', [550, 0]],    ['Vacio', [650, 0]]   ]

all_sprites_matriz_list =  pygame.sprite.Group ()

# ------------------------------- Pantalla de inicio del menu del juego ------------------------------- #
def juego():


    global MATRIZ

    #Imagen de fondos
    #Por ahorita es el fondo blanco
    #background = pygame.image.load('fondo.png').convert()
    #screen.fill(background,[0,0])


    #Matriz de imagen
    matriz_0_dibujo = pygame.image.load('resource/matriz_0.png').convert()


    #Conjunto de enemigos
    avatar_list = pygame.sprite.Group ()

    level_1 = True
    level_2 = False
    level_3 = False

    #Creacion de Avatars segun el nivel que se encuentra
    if level_1:
        for i in range(50):
            avatar = AvartsV0.New_Avart(random.randint(1,4))
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

            for enemy in avatar_list:
                for estado in MATRIZ[ len(MATRIZ)-5 : ] :
                    if estado[0] == 'Vacio' and enemy.posicion_get() [0] == estado [1] [0]:
                        screen.blit(enemy.image_get(),enemy.posicion_get())
                        estado[0] = enemy.type_get()

                    else:
                        pass




        clock.tick(1)
        pygame.display.flip()


def draw_objetcs_matriz():
    global all_sprites_matriz_list
    for draw in all_sprites_matriz_list:
        screen.draw
juego()