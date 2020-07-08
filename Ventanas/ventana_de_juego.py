import pygame,sys,random
from GameV0 import *
from Objetos import AvartsV0
from Objetos import RooksV0

#Variables Globales a Necesitar


#Matriz de posiciones de juego
global MATRIZ, all_sprites_matriz_list, time_to_start, time_last_time_new_enemy
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

time_to_start = pygame.time.get_ticks()/1000

time_last_time_new_enemy = time_to_start








#Parte Funcional del Juego




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
    global avatar_list
    avatar_list = []
    avatar_list_in_game = pygame.sprite.Group ()
    list_ramdom_secs = []

    # Conjunto de rooks
    rook_list = pygame.sprite.Group()

    level_1 = True
    level_2 = False
    level_3 = False

    #Creacion de Avatars segun el nivel que se encuentra
    if level_1:
        # Tiempo de apracion de avatar entre 5 15
        list_ramdom_secs = range(5,15)
        for i in range(50):
            avatar = AvartsV0.New_Avart(random.randint(1,4))
            avatar_list.append(avatar)



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

            draw_objetcs_matriz()

            put_new_enemy(list_ramdom_secs)


            for rook in rook_list:
                for i in range(len(MATRIZ)):
                    for j in MATRIZ[i]:
                        if j[0] == "Vacio":
                            screen.blit(rook.image_get(), rook.position())
                        else:
                            pass






        clock.tick(60)
        pygame.display.flip()

def put_new_enemy(list_ramdom_secs):
    global time_last_time_new_enemy
    random.choice(list_ramdom_secs)
    if 15 == int(pygame.time.get_ticks()//1000 - time_last_time_new_enemy) :
        print('Han pasado',int(pygame.time.get_ticks()//1000 - time_last_time_new_enemy), 'Totalmente',pygame.time.get_ticks()//1000 )
        time_last_time_new_enemy = pygame.time.get_ticks()//1000
        return put_new_enemy_aux()

def put_new_enemy_aux():

    global avatar_list
    done = False
    print()
    print('Me llamaron')
    for enemy in avatar_list:
        for estado in MATRIZ[len(MATRIZ) - 5:]:
            if estado[0] == 'Vacio' and enemy.posicion_get()[0] == estado[1][0]:
                estado[0] = enemy
                avatar_list = avatar_list[1:]
                print('enemigo puesto','Quedan en total sin poner',len(avatar_list))
                done = True
            else:
                #print('Estoy lleno')
                pass

        if done:
            print('termine de poner enemigo')
            print()
            break

def draw_objetcs_matriz():
    global all_sprites_matriz_list,MATRIZ
    for cuadrito in MATRIZ:
        object = cuadrito[0]
        if object != 'Vacio':
            object.draw_me()



juego()