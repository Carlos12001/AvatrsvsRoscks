import pygame,sys,random
from GameV0 import *
from Objetos import AvartsV0
from Objetos import RooksV0
from Objetos import CoinsV0

#Variables Globales a Necesitar
global MATRIZ, all_sprites_matriz_list, time_to_start, time_last_time_new_enemy,all_atacks_in_game
global atacks_avart_0, atacks_avart_1, atacks_avart_2, atacks_avart_3, atacks_avart_4
global atacks_rooks_0, atacks_rooks_1, atacks_rooks_2, atacks_rooks_3, atacks_rooks_4
global avart_0, avart_1, avart_2, avart_3, avart_4
global rook_0, rook_0, rook_0, rook_0, rook_0
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

atacks_avart_0 = pygame.sprite.Group()
atacks_avart_1 = pygame.sprite.Group()
atacks_avart_2 = pygame.sprite.Group()
atacks_avart_3 = pygame.sprite.Group()
atacks_avart_4 = pygame.sprite.Group()

atacks_rooks_0 = pygame.sprite.Group()
atacks_rooks_1 = pygame.sprite.Group()
atacks_rooks_2 = pygame.sprite.Group()
atacks_rooks_3 = pygame.sprite.Group()
atacks_rooks_4 = pygame.sprite.Group()

avart_0 = pygame.sprite.Group()
avart_1 = pygame.sprite.Group()
avart_2 = pygame.sprite.Group()
avart_3 = pygame.sprite.Group()
avart_4 = pygame.sprite.Group()

rook_0 = pygame.sprite.Group()
rook_1 = pygame.sprite.Group()
rook_2 = pygame.sprite.Group()
rook_3 = pygame.sprite.Group()
rook_4 = pygame.sprite.Group()

all_atacks_in_game = pygame.sprite.Group()
all_sprites_matriz_list = pygame.sprite.Group ()

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
    if 1 == int(pygame.time.get_ticks()//1000 - time_last_time_new_enemy) :
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
                put_new_enemy_aux_2(estado[1][0],enemy)
                done = True
                break
            else:
                pass

        if done:

            break

def put_new_enemy_aux_2(pos_x,enemy):
    global avart_0, avart_1, avart_2, avart_3, avart_4
    if pos_x == 250:
        avart_0.add(enemy)
    if pos_x == 350:
        avart_1.add(enemy)
    if pos_x == 450:
        avart_2.add(enemy)
    if pos_x == 550:
        avart_3.add(enemy)
    if pos_x == 650:
        avart_4.add(enemy)


def move_enemy():
    global MATRIZ,game_over
    i_now = 0
    for fila in MATRIZ:
        j_now = 0
        for cuadrito in fila:
            #Revisa si hay personaje
            if cuadrito [0] != 'Vacio':

                #Revisa si es un enemigo
                if cuadrito[0].type_get() == 'Arquero' or cuadrito[0].type_get() == 'Escudero'\
                or cuadrito[0].type_get() == 'Lenador' or cuadrito[0].type_get() == 'Canival':


                    #Revisa si es posible el cambio
                    if i_now-1 >=0 and MATRIZ[i_now-1][j_now][0] == 'Vacio':
                        if cuadrito[0].update(pygame.time.get_ticks()):
                            MATRIZ[i_now-1][j_now][0] = cuadrito[0]
                            cuadrito[0] = 'Vacio'

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

def rook_posicion(tipo,mouse_pos, mouse_click):


    # primer fila

    if 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 90:
        # posicionar cada type_rook en un a posicion estandar
        rectX = 250
        rectY = 0
        set = False

    elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 90:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 0
        set = False

    elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 90:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 0
        set = False

    elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 90:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 0
        set = False

    elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 90:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 0
        set = False

    # segunda fila

    elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 90
        set = False

    elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 90
        set = False

    elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 90
        set = False

    elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 90
        set = False

    elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 90 < mouse_pos[1] < 180:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 90
        set = False


    # tercera fila

    elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 180
        set = False

    elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 180
        set = False

    elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 180
        set = False

    elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 180
        set = False

    elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 180 < mouse_pos[1] < 270:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 180
        set = False


    # cuarta fila

    elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 270
        set = False

    elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 270
        set = False

    elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 270
        set = False

    elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 270
        set = False

    elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 270 < mouse_pos[1] < 360:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 270
        set = False

        # quinta fila

    elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 360
        set = False

    elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 360
        set = False

    elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 360
        set = False

    elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 360
        set = False

    elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 360 < mouse_pos[1] < 450:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 360
        set = False

        # sexta fila

    elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 450
        set = False

    elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 450
        set = False

    elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 450
        set = False

    elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 450
        set = False

    elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 450 < mouse_pos[1] < 540:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 450
        set = False

        # septima fila

    elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 540
        set = False

    elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 540
        set = False

    elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 540
        set = False

    elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 540
        set = False

    elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 540 < mouse_pos[1] < 630:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 540
        set = False

        # octava fila

    elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 630
        set = False

    elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 630
        set = False

    elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 630
        set = False

    elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 630
        set = False

    elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 630 < mouse_pos[1] < 720:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 630
        set = False

    # novena fila

    elif 250 < mouse_pos[0] < 350 and mouse_click[0] == 1 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 250
        rectY = 720
        set = False

    elif 350 < mouse_pos[0] < 450 and mouse_click[0] == 1 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 350
        rectY = 720
        set = False

    elif 450 < mouse_pos[0] < 550 and mouse_click[0] == 1 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 450
        rectY = 720
        set = False

    elif 550 < mouse_pos[0] < 650 and mouse_click[0] == 1 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 550
        rectY = 720
        set = False

    elif 650 < mouse_pos[0] < 750 and mouse_click[0] == 1 and 720 < mouse_pos[1] < 810:
        # posicionar cada self.type_rook en un a posicion estandar
        rectX = 650
        rectY = 720
        set = False

    else:
        set = True
        rectX = 0
        rectY = 0

    put_new_rook( [tipo, set, [rectX, rectY]] )

def put_new_rook(lists):
    global MATRIZ,shop_open
    if not lists [1]:
        for fila in MATRIZ:
            for cuadrito in fila:
                if cuadrito[0] == 'Vacio' and cuadrito[1] == lists[2] :
                    cuadrito[0] = new_rook(lists[0], lists[2])
                    shop_open = True

def new_rook(tipo,pos):

    rook=[]
    if tipo == 5:
        rook = RooksV0.New_Rook(tipo,pos)

    if tipo == 6:
        rook = RooksV0.New_Rook(tipo,pos)

    if tipo == 7:
        rook = RooksV0.New_Rook(tipo,pos)

    if tipo == 8:
        rook = RooksV0.New_Rook(tipo,pos)

    return rook


#Funciones para los ataques
def atacks():
    global MATRIZ, all_atacks_in_game
    global atacks_avart_0,atacks_avart_1,atacks_avart_2,atacks_avart_3,atacks_avart_4
    global atacks_rooks_0,atacks_rooks_1,ataks_rooks_2,atacks_rooks_3,atacks_rooks_4

    for fila in MATRIZ:
        for cuadrito in fila:
            if cuadrito[0] != 'Vacio':
                if not(cuadrito[0].type_get() == 'Arquero' or cuadrito[0].type_get() == 'Escudero'
                                              or cuadrito[0].type_get() == 'Lenador' or cuadrito[0].type_get() == 'Canival'):

                    #Ataque
                    atacking = cuadrito[0].atack(pygame.time.get_ticks())

                    if atacking != '' :
                        if cuadrito[1][0] == 250:
                            atacks_rooks_0.add(atacking)
                            all_atacks_in_game.add(atacking)
                            #atacks_colsion_check(True, cuadrito[0].damage(), cuadrito[1][0])
                        if cuadrito[1][0] == 350:
                            atacks_rooks_1.add(atacking)
                            all_atacks_in_game.add(atacking)
                            #atacks_colsion_check(True, cuadrito[0].damage(), cuadrito[1][0])
                        if cuadrito[1][0] == 450:
                            atacks_rooks_2.add(atacking)
                            all_atacks_in_game.add(atacking)
                            #atacks_colsion_check(True, cuadrito[0].damage(), cuadrito[1][0])
                        if cuadrito[1][0] == 550:
                            atacks_rooks_3.add(atacking)
                            all_atacks_in_game.add(atacking)
                            #atacks_colsion_check(True, cuadrito[0].damage(), cuadrito[1][0])
                        if cuadrito[1][0] == 650:
                            atacks_rooks_4.add(atacking)
                            all_atacks_in_game.add(atacking)
                            #atacks_colsion_check(True, cuadrito[0].damage(), cuadrito[1][0])
                        atacks_colsion_check(True, cuadrito[0].damage(), cuadrito[1][0])

                    else:
                        atacks_colsion_check(True, cuadrito[0].damage(), cuadrito[1][0])

                else:
                    pass

def atacks_move():
    global  all_atacks_in_game
    for atacking in all_atacks_in_game:
        atacking.trayect()

def atacks_colsion_check(who_shots,damage,columna):
    global avart_0, avart_1, avart_2, avart_3, avart_4
    global atacks_rooks_0, atacks_rooks_1, atacks_rooks_2, atacks_rooks_3, atacks_rooks_4
    global MATRIZ, all_atacks_in_game
    #Logica para avatar impacto
    if who_shots:
        colision = {}

        if columna == 250:
            colision = pygame.sprite.groupcollide(avart_0, atacks_rooks_0, False, True)
        elif columna == 350:
            colision = pygame.sprite.groupcollide(avart_1, atacks_rooks_1, False, True)
        elif columna == 450:
            colision = pygame.sprite.groupcollide(avart_2, atacks_rooks_2, False, True)
        elif columna == 550:
            colision = pygame.sprite.groupcollide(avart_3, atacks_rooks_3, False, True)
        elif columna == 650:
            colision = pygame.sprite.groupcollide(avart_4, atacks_rooks_4, False, True)



        if colision != {}:
            done = False
            avatar = list(colision.keys())[0]
            for fila in MATRIZ:
                for cuadrito in fila:
                    if cuadrito[0] != 'Vacio' and columna==cuadrito[1][0]:
                        if cuadrito[0].type_get() == 'Arquero' or cuadrito[0].type_get() == 'Escudero' \
                            or cuadrito[0].type_get() == 'Lenador' or cuadrito[0].type_get() == 'Canival':
                            if avatar.who() == cuadrito[0].who() and cuadrito[0].life( damage) == 'i die':
                                avatar.kill()
                                cuadrito[0] = 'Vacio'
                                done = True
                                break
                            else:
                                done = True
                                break
                if done:
                    break





    pass

#Dibuja el los objetos de la matriz
def draw_objetcs_matriz():
    global all_sprites_matriz_list,MATRIZ
    for fila in MATRIZ:
        for cuadrito in fila:
            object = cuadrito[0]
            if object != 'Vacio':
                object.draw_me(pygame.time.get_ticks())




# ------------------------------- Pantalla de inicio del menu del juego ------------------------------- #


def juego():
    global MATRIZ,all_atacks_in_game


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

    # Cosas que necesita rooks
    type = 0

    # Conjunto de monedas
    global coins
    coins = 100
    global coin_list
    coin_list = []
    for i in range(20):
        coin = CoinsV0.New_Coin(random.randint(1, 3))
        coin_list.append(coin)


    level_1 = True
    level_2 = False
    level_3 = False

    #Creacion de Avatars segun el nivel que se encuentra
    if level_1:
        # Tiempo de apracion de avatar entre 5 15
        list_ramdom_secs = range(5, 15)
        num = 0
        for i in range(50):
            avatar = AvartsV0.New_Avart(random.randint(1,4),num)
            avatar_list.append(avatar)
            num += 1



    global game_over,shop_open
    shop_open = True
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
                for i in MATRIZ:
                    print(i)


                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if shop_open:
                    if coins > 0:           #Hacer global las coins y shop_open, para meter toda la logica de las monedas en funcion
                        if coins >= 50 and sand_button.collidepoint(event.pos):
                            coins -= 50
                            type = 5
                            shop_open = False
                        elif coins >= 100 and rock_button.collidepoint(event.pos):
                            coins -= 100
                            type = 6
                            shop_open = False
                        elif coins >= 150 and fire_button.collidepoint(event.pos):
                            coins -= 150
                            type = 7
                            shop_open = False
                        elif coins >= 150 and water_button.collidepoint(event.pos):
                            coins -= 150
                            type = 8
                            shop_open = False
                        else:
                            coins = coins
                    else:
                        coins = 0
                else:
                     rook_posicion(type,pygame.mouse.get_pos(),[1])   #Hay que quitar si existe un click

                #Logica de quitar rook con otro if y otra funcion checkea donde ocurrio el click y si hay rook

        #Pierde el juego
        for enemy_false in MATRIZ[0]:
            pass
            #if enemy_false[0] !='Vacio': #Agregar logica para verificar si es un Avatar
                #game_over = True
                #import GameV0
                #GameV0.start()



        screen.fill(white)
        pygame.draw.rect(screen, brown, sand_button)
        pygame.draw.rect(screen, lightgreen, rock_button)
        pygame.draw.rect(screen, green, fire_button)

        pygame.draw.rect(screen, purple, water_button)
        text(str(coins), font2,brown, screen,100,50)


        # Primer Nivel
        if level_1:
            screen.blit(matriz_0_dibujo, [250, 0])
            draw_objetcs_matriz()

            #Parte funcional avatrs
            put_new_enemy(list_ramdom_secs)
            move_enemy()

            #Parte funcional coins
            put_new_coin()
            draw_coins()
            kill_coins()

            #Parte funcional para que disparen los rooks
            atacks()
            all_atacks_in_game.draw(screen)
            atacks_move()


        clock.tick(60)
        pygame.display.flip()

juego()
