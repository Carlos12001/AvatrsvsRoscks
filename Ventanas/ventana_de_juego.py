import pygame,sys,random
from GameV0 import *
from Objetos import AvartsV0

#Variables Globales a Necesitar


#Matriz de posiciones de juego
#Variables a utilizar en
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
def juego():


    global MATRIZ

    #Imagen de fondos
    #Por ahorita es el fondo blanco
    #background = pygame.image.load('fondo.png').convert()
    #screen.fill(background,[0,0])


    #Matriz de imagen
    matriz_0_dibujo = pygame.image.load('resource/matriz_0.png').convert()


    #Conjunto de enemigos
    global avatar_list
    avatar_list = []
    avatar_list_in_game = pygame.sprite.Group ()
    list_ramdom_secs = []

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



    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
                exit()
        screen.fill(white)
        if level_1:
            screen.blit(matriz_0_dibujo, [250, 0])

            draw_objetcs_matriz()

            put_new_enemy(list_ramdom_secs)

            move_enemy()






        clock.tick(60)
        pygame.display.flip()

def put_new_enemy(list_ramdom_secs):
    global time_last_time_new_enemy
    if 15 == int(pygame.time.get_ticks()//1000 - time_last_time_new_enemy) :
        time_last_time_new_enemy = pygame.time.get_ticks()//1000
        return put_new_enemy_aux()

def put_new_enemy_aux():

    global avatar_list
    done = False

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

            break

def draw_objetcs_matriz():
    global all_sprites_matriz_list,MATRIZ
    for cuadrito in MATRIZ:
        object = cuadrito[0]
        if object != 'Vacio':
            object.draw_me()

def move_enemy():
    global MATRIZ
    for cuadrito in MATRIZ:
        if cuadrito [0] != 'Vacio':
            if cuadrito[0].type_get() == 'Arquero' or cuadrito[0].type_get() == 'Escudero'\
            or cuadrito[0].type_get() == 'Lenador' or cuadrito[0].type_get() == 'Canival':
                cuadrito[0].update()
                cuadrito[0] = 'Vacio'

juego()