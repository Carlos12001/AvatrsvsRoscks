import pygame,sys,random
from GameV0 import *
from Objetos import AvartsV0
from Objetos import RooksV0

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
coins = 500
def juego():


    global MATRIZ

    #Imagen de fondos
    #Por ahorita es el fondo blanco
    #background = pygame.image.load('fondo.png').convert()
    #screen.fill(background,[0,0])


    #Matriz de imagen
    matriz_0_dibujo = pygame.image.load('resource/matriz_0.png').convert()

    # botones tienda

    sand_button = pygame.Rect(0,500,100,80)
    rock_button = pygame.Rect(0,580,100,80)
    fire_button = pygame.Rect(0,660,100,80)
    water_button =pygame.Rect(0,740,100,80)
    #Conjunto de enemigos
    avatar_list = pygame.sprite.Group ()

    # Conjunto de rooks
    rook_list = pygame.sprite.Group()

    level_1 = True
    level_2 = False
    level_3 = False

    #Creacion de Avatars segun el nivel que se encuentra
    if level_1:
        for i in range(50):
            avatar = AvartsV0.New_Avart(random.randint(1,4))
            avatar_list.add(avatar)

    # Tienda


    # Creacion de Rooks segun donde es presionado

    def new_rook(coins, pos_rook):
        if coins == 0:
            print("sin fondos")# hacer una texto que diga sin monedas
        elif coins >= 50 and pos_rook[0] == 5:
            coins -= 50
            print(coins)
            # colocar el rook de arena
            rook = RooksV0.Rooks(pos_rook)
            rook.position()
            print(rook)
            rook_list.add(rook)
            print(rook_list)
        elif coins >= 100 and pos_rook[0] == 6:
            coins -= 100
            # colocar el rook de roca
            rook = RooksV0.Rooks(pos_rook)
            rook_list.add(rook)
        elif coins >= 150 and pos_rook[0] == 7:
            coins -= 150
            # colocar el rook de fuego
            rook = RooksV0.Rooks(pos_rook)
            rook_list.add(rook)
        elif coins >= 150 and pos_rook[0] == 8:
            coins -= 150
            print(coins)
            # colocar el rook de agua
            rook = RooksV0.Rooks(pos_rook)
            rook_list.add(rook)

    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sand_button.collidepoint(event.pos):
                    pos_rook = [5, [event.pos[0], event.pos[1]]]  # revisar coordenadas
                    print("sand")
                    new_rook(coins, pos_rook)
                elif rock_button.collidepoint(event.pos):
                    pos_rook = [6, [event.pos[0], event.pos[1]]]  # revisar coordenadas
                    print("rock")
                    new_rook(coins, pos_rook)
                elif fire_button.collidepoint(event.pos):
                    pos_rook = [7, [event.pos[0], event.pos[1]]]  # revisar coordenadas
                    print("fire")
                    new_rook(coins, pos_rook)
                elif water_button.collidepoint(event.pos):
                    pos_rook = [8, [event.pos[0], event.pos[1]]]  # revisar coordenadas
                    print(pos_rook)
                    print("water")
                    new_rook(coins, pos_rook)

        screen.fill(white)
        pygame.draw.rect(screen, brown, sand_button)
        pygame.draw.rect(screen, lightgreen, rock_button)
        pygame.draw.rect(screen, green, fire_button)
        pygame.draw.rect(screen, purple, water_button)

        if level_1:
            screen.blit(matriz_0_dibujo, [250, 0])
            for enemy in avatar_list:
                for estado in MATRIZ[ len(MATRIZ)-5 : ] :
                    if estado[0] == 'Vacio' and enemy.posicion_get() [0] == estado [1] [0]:
                        screen.blit(enemy.image_get(),enemy.posicion_get())
                        estado[0] = enemy.type_get()

                    else:
                        pass

            for rook in rook_list:
                for i in range(len(MATRIZ)):
                    for j in MATRIZ[i]:
                        if j[0] == "Vacio":
                            screen.blit(rook.image_get(), rook.position())
                        else:
                            pass




        clock.tick(2)
        pygame.display.flip()


def draw_objetcs_matriz():
    global all_sprites_matriz_list
    for draw in all_sprites_matriz_list:
        screen.draw
juego()