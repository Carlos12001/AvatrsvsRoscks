import pygame,sys,random
from GameV0 import *
from Objetos import AvartsV0
from Objetos import RooksV0
from Objetos import CoinsV0

#Variables Globales a Necesitar
global level_1, level_2, level_3, MATRIZ, time_to_start, time_last_time_new_enemy, num_rook



level_1 = True
level_2 = False
level_3 = False


#Matriz de posiciones de juego
MATRIZ = [    [['Vacio', [250,   0]],    ['Vacio', [350,   0]],   ['Vacio', [450,    0]],    ['Vacio', [550,   0]],    ['Vacio', [650,   0]]],
              [['Vacio', [250,  90]],    ['Vacio', [350,  90]],   ['Vacio', [450,   90]],    ['Vacio', [550,  90]],    ['Vacio', [650,  90]]],
              [['Vacio', [250, 180]],    ['Vacio', [350, 180]],   ['Vacio', [450,  180]],    ['Vacio', [550, 180]],    ['Vacio', [650, 180]]],
              [['Vacio', [250, 270]],    ['Vacio', [350, 270]],   ['Vacio', [450,  270]],    ['Vacio', [550, 270]],    ['Vacio', [650, 270]]],
              [['Vacio', [250, 360]],    ['Vacio', [350, 360]],   ['Vacio', [450,  360]],    ['Vacio', [550, 360]],    ['Vacio', [650, 360]]],
              [['Vacio', [250, 450]],    ['Vacio', [350, 450]],   ['Vacio', [450,  450]],    ['Vacio', [550, 450]],    ['Vacio', [650, 450]]],
              [['Vacio', [250, 540]],    ['Vacio', [350, 540]],   ['Vacio', [450,  540]],    ['Vacio', [550, 540]],    ['Vacio', [650, 540]]],
              [['Vacio', [250, 630]],    ['Vacio', [350, 630]],   ['Vacio', [450,  630]],    ['Vacio', [550, 630]],    ['Vacio', [650, 630]]],
              [['Vacio', [250, 720]],    ['Vacio', [350, 720]],   ['Vacio', [450,  720]],    ['Vacio', [550, 720]],    ['Vacio', [650, 720]]]   ]

matrizcoin = [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None]]

#Lista de objetos en el juego
list_atacks_avart = pygame.sprite.Group()

list_atacks_rooks = pygame.sprite.Group()

list_avarts_in_game = pygame.sprite.Group()

list_rooks_in_game = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
num_rook = 1000 

time_to_start = pygame.time.get_ticks()/1000

time_last_time_new_enemy = time_to_start

time_last_time_new_coin = time_to_start


# -------------------------------------- Parte Funcional del Juego -------------------------------------- #

# funcion texto
def text(text, font, color, surface, x, y):
    txtobj = font.render(text, 1, color)
    txtrect = txtobj.get_rect()
    txtrect.center = (x, y)
    surface.blit(txtobj, txtrect)

# Funciones para el funcionamiento de los avatars

def put_new_enemy(list_ramdom_secs):
    global time_last_time_new_enemy
    if random.choice(list_ramdom_secs) == int(pygame.time.get_ticks()//1000 - time_last_time_new_enemy) :
        time_last_time_new_enemy = pygame.time.get_ticks()//1000
        return put_new_enemy_aux()

def put_new_enemy_aux():

    global avatar_list
    done = False

    for enemy in avatar_list:
        for estado in MATRIZ [8]:
            if estado[0] == 'Vacio' and enemy.posicion_get()[0] == estado[1][0]:
                estado[0] = enemy
                avatar_list = avatar_list[1:]
                list_avarts_in_game.add(enemy)
                done = True
                break
            else:
                pass

        if done:

            break

def move_enemy():
    global MATRIZ,game_over
    i_now = 0
    for fila in MATRIZ:
        j_now = 0
        for cuadrito in fila:
            #Revisa si hay personaje
            if cuadrito [0] != 'Vacio':

                #Revisa si
                if cuadrito[0].type_get() == 'Arquero' or cuadrito[0].type_get() == 'Escudero'\
                or cuadrito[0].type_get() == 'Lenador' or cuadrito[0].type_get() == 'Canival':


                    #Revisa si es posible el cambio
                    if i_now-1 >=0 and MATRIZ[i_now-1][j_now][0] == 'Vacio':
                        if cuadrito[0].update(pygame.time.get_ticks()):
                            MATRIZ[i_now-1][j_now][0] = cuadrito[0]
                            cuadrito[0] = 'Vacio'
            j_now += 1
        i_now += 1

def atacks_avarts():
    global MATRIZ
    done = False

    i_now = 0
    for fila in MATRIZ:
        j_now = 0
        for cuadrito in fila:
            if cuadrito[0] != 'Vacio':

                if cuadrito[0].type_get() == 'Arquero' or cuadrito[0].type_get() == 'Escudero':
                    atacking = cuadrito[0].atack(pygame.time.get_ticks())
                    if atacking != '':
                        list_atacks_avart.add(atacking)
                        break
                elif cuadrito[0].type_get() == 'Lenador' or cuadrito[0].type_get() == 'Canival':
                    if i_now - 1 >= 0 and MATRIZ[i_now - 1][j_now][0] != 'Vacio':
                        if MATRIZ[i_now - 1][j_now][0].type_get() == 'Sand' \
                                or MATRIZ[i_now - 1][j_now][0].type_get() == 'Rock' \
                                or MATRIZ[i_now - 1][j_now][0].type_get() == 'Fire' \
                                or MATRIZ[i_now - 1][j_now][0].type_get() == 'Water':
                            atacking = cuadrito[0].atack(pygame.time.get_ticks())
                            if atacking != '':
                                list_atacks_avart.add(atacking)
                                all_sprites.add(atacking)
                                break

            j_now += 1

        i_now += 1

# Funciones para el funcionamiento de las monedas

def put_new_coin():
    global time_last_time_new_coin
    global coin_list
    time = random.randint(5,10)
    if time == int(pygame.time.get_ticks()//1000 - time_last_time_new_coin) :
        time_last_time_new_coin = pygame.time.get_ticks()//1000
        return put_new_coin_aux()

def put_new_coin_aux():
    global  matrizcoin,coin_list
    done = False
    for coin in coin_list:
        for coin2 in matrizcoin:
            if coin2[0] == None:
                coin2[0] = coin
                coin_list = coin_list[1:]
                done = True
                break
            else:
                pass
        if done:
            break

def draw_coins ():
    global matrizcoin
    for moneda in matrizcoin:
        coins = moneda[0]
        if coins != None:
            coins.draw_me()

def kill_coins ():
    global matrizcoin
    global coins
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    for moneda in matrizcoin:
        coin_obj = moneda[0]
        if coin_obj == None:
            pass
        elif coin_obj != None:
            coin_pos = coin_obj.posicion_get()
            coin_value = coin_obj.value_get()
            if coin_pos[0] <= mouse_pos[0] <= coin_pos[0] + 50 and mouse_click[0] == 1 and coin_pos[1] <= mouse_pos[1] <= coin_pos[1] + 50:
                if coin_value == 25:
                    moneda[0] = None
                    coins += 25
                    break
                elif coin_value == 50:
                    moneda[0] = None
                    coins += 50
                    break
                elif coin_value == 100:
                    moneda[0] = None
                    coins += 100
                    break

# Funciones para el funcionamiento de los rooks

def rook_posicion( tipo, mouse_pos):

    # primer fila

    if 250 < mouse_pos[0] < 350 and 0 < mouse_pos[1] < 90:
        # posicionar cada type_rook en un a posicion estandar
        rectX = 250
        rectY = 0
        set = False

    elif 350 < mouse_pos[0] < 450 and 0 < mouse_pos[1] < 90:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 0
        set = False

    elif 450 < mouse_pos[0] < 550 and 0 < mouse_pos[1] < 90:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 0
        set = False

    elif 550 < mouse_pos[0] < 650 and 0 < mouse_pos[1] < 90:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 0
        set = False

    elif 650 < mouse_pos[0] < 750 and 0 < mouse_pos[1] < 90:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 0
        set = False

    # segunda fila

    elif 250 < mouse_pos[0] < 350 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 90
        set = False

    elif 350 < mouse_pos[0] < 450 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 90
        set = False

    elif 450 < mouse_pos[0] < 550 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 90
        set = False

    elif 550 < mouse_pos[0] < 650 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 90
        set = False

    elif 650 < mouse_pos[0] < 750 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 90
        set = False


    # tercera fila

    elif 250 < mouse_pos[0] < 350 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 180
        set = False

    elif 350 < mouse_pos[0] < 450 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 180
        set = False

    elif 450 < mouse_pos[0] < 550 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 180
        set = False

    elif 550 < mouse_pos[0] < 650 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 180
        set = False

    elif 650 < mouse_pos[0] < 750 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 180
        set = False


    # cuarta fila

    elif 250 < mouse_pos[0] < 350 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 270
        set = False

    elif 350 < mouse_pos[0] < 450 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 270
        set = False

    elif 450 < mouse_pos[0] < 550 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 270
        set = False

    elif 550 < mouse_pos[0] < 650 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 270
        set = False

    elif 650 < mouse_pos[0] < 750 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 270
        set = False

        # quinta fila

    elif 250 < mouse_pos[0] < 350 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 360
        set = False

    elif 350 < mouse_pos[0] < 450 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 360
        set = False

    elif 450 < mouse_pos[0] < 550 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 360
        set = False

    elif 550 < mouse_pos[0] < 650 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 360
        set = False

    elif 650 < mouse_pos[0] < 750 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 360
        set = False

        # sexta fila

    elif 250 < mouse_pos[0] < 350 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 450
        set = False

    elif 350 < mouse_pos[0] < 450 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 450
        set = False

    elif 450 < mouse_pos[0] < 550 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 450
        set = False

    elif 550 < mouse_pos[0] < 650 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 450
        set = False

    elif 650 < mouse_pos[0] < 750 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 450
        set = False

        # septima fila

    elif 250 < mouse_pos[0] < 350 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 540
        set = False

    elif 350 < mouse_pos[0] < 450 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 540
        set = False

    elif 450 < mouse_pos[0] < 550 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 540
        set = False

    elif 550 < mouse_pos[0] < 650 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 540
        set = False

    elif 650 < mouse_pos[0] < 750 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 540
        set = False

        # octava fila

    elif 250 < mouse_pos[0] < 350 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 630
        set = False

    elif 350 < mouse_pos[0] < 450 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 630
        set = False

    elif 450 < mouse_pos[0] < 550 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 630
        set = False

    elif 550 < mouse_pos[0] < 650 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 630
        set = False

    elif 650 < mouse_pos[0] < 750 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 630
        set = False

    # novena fila

    elif 250 < mouse_pos[0] < 350 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 720
        set = False

    elif 350 < mouse_pos[0] < 450 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 720
        set = False

    elif 450 < mouse_pos[0] < 550 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 720
        set = False

    elif 550 < mouse_pos[0] < 650 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 720
        set = False

    elif 650 < mouse_pos[0] < 750 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 720
        set = False

    else:
        rectX = 0
        rectY = 0
        set = True

    put_new_rook( [tipo, set, [rectX, rectY]] )

def put_new_rook(lists):
    global MATRIZ,shop_open
    if not lists [1]:
        for fila in MATRIZ:
            for cuadrito in fila:
                if cuadrito[0] == 'Vacio' and cuadrito[1] == lists[2] :
                    
                    cuadrito[0] = new_rook(lists[0], lists[2])
                    list_rooks_in_game.add(cuadrito[0])
                    all_sprites.add(cuadrito[0])
                    shop_open = True

def new_rook(tipo,pos):
    global num_rook
    rook = []
    if tipo == 5:
        rook = RooksV0.New_Rook( tipo, pos, num_rook )

    if tipo == 6:
        rook = RooksV0.New_Rook( tipo, pos, num_rook )

    if tipo == 7:
        rook = RooksV0.New_Rook( tipo, pos, num_rook )

    if tipo == 8:
        rook = RooksV0.New_Rook( tipo, pos, num_rook )
    num_rook += 1
    return rook

def atacks_rooks():
    global MATRIZ
    for fila in MATRIZ:
        for cuadrito in fila:

            if cuadrito[0] != 'Vacio':

                if not(cuadrito[0].type_get() == 'Arquero' or cuadrito[0].type_get() == 'Escudero'
                    or cuadrito[0].type_get() == 'Lenador' or cuadrito[0].type_get() == 'Canival'):
                    #Ataque
                    atacking = cuadrito[0].atack(pygame.time.get_ticks())
                    if atacking != '' :
                        list_atacks_rooks.add(atacking)
                        all_sprites(atacking)

def click_posicion(mouse_pos):
    # global click
    # primer fila

    if 250 < mouse_pos[0] < 350 and 0 < mouse_pos[1] < 90:
        # posicionar cada type_rook en un a posicion estandar
        rectX = 250
        rectY = 0

    elif 350 < mouse_pos[0] < 450 and 0 < mouse_pos[1] < 90:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 0

    elif 450 < mouse_pos[0] < 550 and 0 < mouse_pos[1] < 90:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 0

    elif 550 < mouse_pos[0] < 650 and 0 < mouse_pos[1] < 90:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 0

    elif 650 < mouse_pos[0] < 750 and 0 < mouse_pos[1] < 90:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 0

    # segunda fila

    elif 250 < mouse_pos[0] < 350 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 90

    elif 350 < mouse_pos[0] < 450 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 90

    elif 450 < mouse_pos[0] < 550 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 90

    elif 550 < mouse_pos[0] < 650 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 90

    elif 650 < mouse_pos[0] < 750 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 90

    # tercera fila

    elif 250 < mouse_pos[0] < 350 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 180

    elif 350 < mouse_pos[0] < 450 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 180

    elif 450 < mouse_pos[0] < 550 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 180

    elif 550 < mouse_pos[0] < 650 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 180

    elif 650 < mouse_pos[0] < 750 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 180

    # cuarta fila

    elif 250 < mouse_pos[0] < 350 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 270

    elif 350 < mouse_pos[0] < 450 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 270

    elif 450 < mouse_pos[0] < 550 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 270

    elif 550 < mouse_pos[0] < 650 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 270

    elif 650 < mouse_pos[0] < 750 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 270

        # quinta fila

    elif 250 < mouse_pos[0] < 350 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 360

    elif 350 < mouse_pos[0] < 450 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 360

    elif 450 < mouse_pos[0] < 550 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 360

    elif 550 < mouse_pos[0] < 650 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 360

    elif 650 < mouse_pos[0] < 750 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 360

        # sexta fila

    elif 250 < mouse_pos[0] < 350 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 450

    elif 350 < mouse_pos[0] < 450 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 450

    elif 450 < mouse_pos[0] < 550 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 450

    elif 550 < mouse_pos[0] < 650 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 450

    elif 650 < mouse_pos[0] < 750 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 450

        # septima fila

    elif 250 < mouse_pos[0] < 350 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 540

    elif 350 < mouse_pos[0] < 450 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 540

    elif 450 < mouse_pos[0] < 550 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 540

    elif 550 < mouse_pos[0] < 650 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 540

    elif 650 < mouse_pos[0] < 750 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 540

        # octava fila

    elif 250 < mouse_pos[0] < 350 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 630

    elif 350 < mouse_pos[0] < 450 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 630

    elif 450 < mouse_pos[0] < 550 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 630

    elif 550 < mouse_pos[0] < 650 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 630

    elif 650 < mouse_pos[0] < 750 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 630

    # novena fila

    elif 250 < mouse_pos[0] < 350 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 720

    elif 350 < mouse_pos[0] < 450 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 720

    elif 450 < mouse_pos[0] < 550 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 720

    elif 550 < mouse_pos[0] < 650 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 720

    elif 650 < mouse_pos[0] < 750 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 720

    else:

        rectX = 0
        rectY = 0

    quit_pos = [rectX, rectY]
    quit_rook(quit_pos)

def quit_rook(quit_pos):
    global MATRIZ
    global quit_rook_var
    quit_rook_var = False
    for fila in MATRIZ:
        for cuadrito in fila:
            if cuadrito[0] != "Vacio" and cuadrito[1] == quit_pos:
                if cuadrito[0].type_get() == "Sand" or cuadrito[0].type_get() == "Rock" or cuadrito[
                    0].type_get() == "Fire" or cuadrito[0].type_get() == "Water":
                    cuadrito[0].kill()
                    cuadrito[0] = "Vacio"
                else:
                    print("no se puede eliminar avatar")  # ver como indicar esto
            elif cuadrito[0] == "Vacio":
                pass


#Funciones para los ataques

def atacks_move():
    for atacking_rook in list_atacks_rooks:
        atacking_rook.update()

    for atacking_avart in list_atacks_avart:
        atacking_avart.update()

def atacks_colsion_check_avart():
    global MATRIZ,coins

    #Logica para avatar impacto
    colisicion_avarts = pygame.sprite.groupcollide(list_avarts_in_game,list_atacks_rooks,False,True)
    if colisicion_avarts != {}:
        atacking = list(colisicion_avarts.values())[0][0].get_damage()
        list(colisicion_avarts.values())[0][0].kill()
        avatar_victimin = list(colisicion_avarts.keys())[0]

        if avatar_victimin.life(atacking) == 'i die':
            num = avatar_victimin.who()
            coins += 100
            for fila in MATRIZ:
                for cuadrito in fila:
                    if cuadrito[0] != 'Vacio':
                        if  cuadrito[0].who() == num:
                            cuadrito[0].kill()
                            avatar_victimin.kill()
                            cuadrito [0] = 'Vacio'
                    elif cuadrito[0] =='Vacio':
                        cuadrito[0] = 'Vacio'

def atacks_colsion_check_rook():
    global MATRIZ

    #Logica para avatar impacto
    colisicion_avarts = pygame.sprite.groupcollide(list_rooks_in_game, list_atacks_avart, False, True)
    if colisicion_avarts != {}:
        atacking = list(colisicion_avarts.values())[0][0].get_damage()
        list(colisicion_avarts.values())[0][0].kill()
        rook_victimin = list(colisicion_avarts.keys())[0]

        if rook_victimin.life(atacking) == 'i die':
            num = rook_victimin.who()

            for fila in MATRIZ:
                for cuadrito in fila:
                    if cuadrito[0] != 'Vacio':
                        if cuadrito[0].who() == num:
                            cuadrito[0].kill()
                            rook_victimin.kill()
                            cuadrito[0] = 'Vacio'
                    elif cuadrito[0] == 'Vacio':
                        cuadrito[0] = 'Vacio'

#Dibuja el los objetos de la matriz
def draw_objetcs_matriz():
    global MATRIZ
    for fila in MATRIZ:
        for cuadrito in fila:
            object = cuadrito[0]
            if object != 'Vacio':
                object.draw_me(pygame.time.get_ticks())

#Funcion para quitar el nombre de la lista
def quit_name(name):
    global player_name
    ruta = "player_name.txt"
    file = open(ruta,"w")
    for line in file:
        if line == player_name:
            line = ""

#Limpia la matriz y la lista de objetos

def limpiar_matriz():
    global MATRIZ
    for fila in MATRIZ:
        for cuadrtito in fila:
            cuadrtito[0] = 'Vacio'
    for sprite in all_sprites:
        sprite.kill()


# ------------------------------- Pantalla de inicio del menu del juego ------------------------------- #


def juego():
    global MATRIZ, level_1, level_2, level_3

    # Matriz de imagen
    matriz_0_dibujo = pygame.image.load('resource/matriz_0.png').convert()

    # botones tienda
    sand_button = pygame.Rect(0, 500, 100, 80)
    rock_button = pygame.Rect(0, 580, 100, 80)
    fire_button = pygame.Rect(0, 660, 100, 80)
    water_button =pygame.Rect(0, 740, 100, 80)
    quit_button = pygame.Rect(900, 500, 100, 80)

    #Conjunto de enemigos
    global avatar_list
    avatar_list = []
    avatar_list_in_game = pygame.sprite.Group ()
    list_ramdom_secs = []

    # Cosas que necesita rooks
    tipo = 0

    # Conjunto de monedas
    global coins
    coins = 100
    global coin_list
    coin_list = []
    for i in range(20):
        coin = CoinsV0.New_Coin(random.randint(1, 3))
        coin_list.append(coin)
        all_sprites.add(coin)




    #Creacion de Avatars segun el nivel que se encuentra
    if level_1:
        # Tiempo de apracion de avatar entre 5 15
        list_ramdom_secs = range(1, 2)
        num = 0
        for i in range(1):
            avatar = AvartsV0.New_Avart(1,num)#random.randint(1,4),num)
            avatar_list.append(avatar)
            num += 1
            all_sprites.add(avatar)


    global game_over,shop_open, quit_rook_var
    shop_open = True
    game_over = False
    quit_rook_var = False

    while not game_over:
        for event in pygame.event.get():

            #Salida abruta del juego
            if event.type == pygame.QUIT:
                game_over=True
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                #Valida si presiono el boton de quitar el rook
                if quit_button.collidepoint(event.pos):
                    quit_rook_var = True
                elif quit_rook_var:
                    mouse_pos = pygame.mouse.get_pos()
                    click_posicion(mouse_pos)

               #Valida si presiono el boton de presionar un rook
                elif shop_open:
                    if coins > 0:           #Hacer global las coins y shop_open, para meter toda la logica de las monedas en funcion
                        if coins >= 50 and sand_button.collidepoint(event.pos):
                            coins -= 50
                            tipo = 5
                            shop_open = False
                            quit_rook_var = False
                        elif coins >= 100 and rock_button.collidepoint(event.pos):
                            coins -= 100
                            tipo = 6
                            shop_open = False
                            quit_rook_var = False
                        elif coins >= 150 and fire_button.collidepoint(event.pos):
                            coins -= 150
                            tipo = 7
                            shop_open = False
                            quit_rook_var = False
                        elif coins >= 150 and water_button.collidepoint(event.pos):
                            coins -= 150
                            tipo = 8
                            shop_open = False
                            quit_rook_var = False
                        else:
                            coins = coins
                    else:
                        coins = 0

                else:
                    rook_posicion(tipo,pygame.mouse.get_pos())


        #Pierde el juego
        for enemy_false in MATRIZ[0]:

            if enemy_false[0] != 'Vacio':

                if enemy_false[0].type_get() == 'Arquero' or  enemy_false[0].type_get() == 'Escudero' or enemy_false[0].type_get() == 'Canival' or enemy_false[0].type_get()=='Lenador':

                    game_over = True
                    import GameV0
                    limpiar_matriz()
                    GameV0.start()


        #Logiga para ganar

        screen.fill(white)
        pygame.draw.rect(screen, brown, sand_button)
        pygame.draw.rect(screen, lightgreen, rock_button)
        pygame.draw.rect(screen, green, fire_button)
        pygame.draw.rect(screen, purple, water_button)
        pygame.draw.rect(screen, darkpurple, quit_button)
        text(str(coins), font2,brown, screen,100,50)


        # Primer Nivel
        if level_1:
            # Revisa las colisiones
            atacks_colsion_check_avart()
            atacks_colsion_check_rook()


            screen.blit(matriz_0_dibujo, [250, 0])
            draw_objetcs_matriz()

            # Parte funcional para que disparen los rooks
            atacks_rooks()
            list_atacks_rooks.draw(screen)
            #atacks_move()

            # Parte funcional para que disparen los avatars
            atacks_avarts()
            list_atacks_avart.draw(screen)
            atacks_move()
            #Parte funcional avatrs
            put_new_enemy(list_ramdom_secs)
            move_enemy()

            #Parte funcional coins
            put_new_coin()
            draw_coins()
            kill_coins()







        clock.tick(60)
        pygame.display.flip()

juego()
