import random, pickle
from GameV0 import *
from Objetos import AvartsV0
from Objetos import CoinsV0
from Objetos import RooksV0

#Variables Globales a Necesitar
global  MATRIZ,  matrizcoin, save, time_to_start, time_last_time_new_enemy, num_rook, levels, one_time_upload_levels, list_ramdom_secs, avatar_list, coins, coin_list

#Matriz de posiciones de juego
MATRIZ = [      [['Vacio', [250,   0]],    ['Vacio', [350,   0]],   ['Vacio', [450,    0]],    ['Vacio', [550,   0]],    ['Vacio', [650,   0]]],
                [['Vacio', [250,  90]],    ['Vacio', [350,  90]],   ['Vacio', [450,   90]],    ['Vacio', [550,  90]],    ['Vacio', [650,  90]]],
                [['Vacio', [250, 180]],    ['Vacio', [350, 180]],   ['Vacio', [450,  180]],    ['Vacio', [550, 180]],    ['Vacio', [650, 180]]],
                [['Vacio', [250, 270]],    ['Vacio', [350, 270]],   ['Vacio', [450,  270]],    ['Vacio', [550, 270]],    ['Vacio', [650, 270]]],
                [['Vacio', [250, 360]],    ['Vacio', [350, 360]],   ['Vacio', [450,  360]],    ['Vacio', [550, 360]],    ['Vacio', [650, 360]]],
                [['Vacio', [250, 450]],    ['Vacio', [350, 450]],   ['Vacio', [450,  450]],    ['Vacio', [550, 450]],    ['Vacio', [650, 450]]],
                [['Vacio', [250, 540]],    ['Vacio', [350, 540]],   ['Vacio', [450,  540]],    ['Vacio', [550, 540]],    ['Vacio', [650, 540]]],
                [['Vacio', [250, 630]],    ['Vacio', [350, 630]],   ['Vacio', [450,  630]],    ['Vacio', [550, 630]],    ['Vacio', [650, 630]]],
                [['Vacio', [250, 720]],    ['Vacio', [350, 720]],   ['Vacio', [450,  720]],    ['Vacio', [550, 720]],    ['Vacio', [650, 720]]]       ]


#Matriz de monedas
matrizcoin = [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None]]

#Variables con la funcionalidad de los niveles

levels = [ True, True, True ]

one_time_upload_levels = [ True, True, True ]

#Rango de secs aleatorio
list_ramdom_secs = 0

#Lista de objetos en el juego
list_atacks_avart = pygame.sprite.Group()

list_atacks_rooks = pygame.sprite.Group()

list_avarts_in_game = pygame.sprite.Group()

list_rooks_in_game = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

#Numero de Moendas en el juego
coins = 100

#Lista de avarts que faltan de poner
avatar_list = []

#Numero de identificador del Rook
num_rook = 1001

#Variables relacionadas con el tiempo
total_time_in_game = 0

time_to_start = pygame.time.get_ticks()/1000

time_last_time_new_enemy = time_to_start

time_last_time_new_coin = time_to_start


# -------------------------------------- Parte Funcional del Juego -------------------------------------- #

#---Textos---
def text(text, font, color, surface, x, y, backgrounf=None):
    txtobj = font.render(text, 1, color, backgrounf)
    txtrect = txtobj.get_rect()
    txtrect.center = (x, y)
    surface.blit(txtobj, txtrect)

#Logica para el guardado

def login():

    # Rutas y Archivos que necesita
    ruta_1 = "Data/game_save.txt"
    ruta_2 = "Data/player_name.txt"
    file_save = open(ruta_1, 'r')
    file_name = open(ruta_2, 'r')

    data_4 = open('Data/levels', 'rb')
    data_5 = open('Data/MATRIZ','rb')

    #1 Resiva si Existe una partida cargada
    boolean_save = file_save.readlines() [0]
    boolean_save = boolean_save[:len(boolean_save)-1]

    #3 Get the last player who save
    file_save.seek(0)
    player_save = file_save.readlines()  [2]
    player_save = player_save[:len(player_save)-1]


    #2 Nombre del player
    player_name = file_name.readlines()  [0]


    if bool( boolean_save ) and player_name == player_save :

        #4 Logica para cargar niveles
        load_aux_1(pickle.load(data_4))

        #5 Poner el tiempo total del juego
        file_save.seek(0)
        line_5 =   file_save.readlines()  [4]
        line_5 = line_5 [:len(line_5)-1]
        load_aux_2( float( line_5 ) )

        #6 logica para poner en matriz los elementos, volver a llamar a all_avarts_in_game, all_rooks_in_game, coin_list y all_sprites
        data_MATRIZ = pickle.load(data_5)

        # 7 numero de avarts que quedaban por poner
        file_save.seek(0)
        line_7 = file_save.readlines()[6]
        line_7 = line_7[:len(line_7) - 1]

        #9 numero de rook por el cual iba
        file_save.seek(0)
        line_9 = file_save.readlines()[8]
        line_9 = line_9[:len(line_9) - 1]

        load_aux_3( data_MATRIZ, int(line_7), int(line_9) )

        # linea 11 de monedas en el juego
        file_save.seek(0)
        line_11 = file_save.readlines()[10]
        line_11 = line_11[:len(line_11) - 1]
        load_aux_4( int( line_11 ) )

def load_aux_1  ( lista ):
    global one_time_upload_levels, levels, list_ramdom_secs

    if lista[0] :
        levels = [ True, True, True ]
        one_time_upload_levels = [ False, True, True ]
        list_ramdom_secs = range(10, 14)     #Ahorita se quita
    elif lista[1] :
        levels = [ False, True, True ]
        one_time_upload_levels = [ False, False, True ]
        list_ramdom_secs = range(4, 8)     #Ahorita se quita
    else:
        levels = [ False, False, True ]
        one_time_upload_levels = [ False, False, False ]
        list_ramdom_secs = range(1, 3)   #Ahorita se quita

def load_aux_2 ( num ):
    global total_time_in_game
    total_time_in_game += num

def  load_aux_3( m,  num1,  num2 ):
    global MATRIZ, num_rook, levels
    #Pone el numero de rook
    num_rook = num2 + 1000
    num2_aux = num2

    #Revisa cuantos avarts quedan en el juego
    if levels[0]:
        num1_aux = num1
        num_avart = 50 - num1

    elif levels[1]:
        num1_aux = num1
        num_avart = 70 - num1

    else:
        num1_aux = num1
        num_avart = 120 - num1
    
    
    for elements in m:
        for fila in MATRIZ:
            for cuadrito in fila:
                name_tipo =  elements[0]

                #Logica para saber que tipo era
                if name_tipo == 'Arquero':
                    tipo = 1
                elif name_tipo == 'Escudero':
                    tipo = 2
                elif name_tipo == 'Lenador':
                    tipo = 3
                elif name_tipo == 'Canival':
                    tipo = 4
                elif name_tipo == 'Sand':
                    tipo = 5
                elif name_tipo == 'Rock':
                    tipo = 6
                elif name_tipo == 'Fire':
                    tipo = 7
                elif name_tipo == 'Water':
                    tipo = 8

                #Logica que posiciona si es avart
                if 1<=tipo<=4 and (cuadrito[1][0] == elements[1][0]) and (cuadrito[1][1] == elements[1][1]+20) and num1_aux != 0:
                    avart = AvartsV0.New_Avart( tipo, num1_aux )
                    num1_aux -= 1
                    avart.set_guardado( elements[1], elements[2] )
                    list_avarts_in_game.add(avart)
                    all_sprites.add(avart)
                    cuadrito[0] = avart



                #Logica para ponersi es rook
                elif 5<=tipo<=8 and (cuadrito[1][0] == elements[1][0]) and (cuadrito[1][1] == elements[1][1]) and num2_aux != 1000:
                    rook = RooksV0.New_Rook( tipo, cuadrito[1] ,num2_aux )
                    num2_aux -= 1
                    rook.set_guardado( elements[2] )
                    list_rooks_in_game.add(rook)
                    all_sprites.add(rook)
                    cuadrito[0] = rook


                #Si el cuadrito no tiene la misma posicion
                else:
                    pass


    #Crea los avarts restantes en avart list
    create_enemy( num1, num_avart )

def load_aux_4 ( num ):
    global coins
    create_new_coins(12)
    coins = num

def save():
    global MATRIZ, one_time_upload_levels, total_time_in_game, time_to_start, avatar_list, coins, game_over

    #Rutas y Archivos que necesita
    ruta_1 = "Data/game_save.txt"
    ruta_2 = "Data/player_name.txt"
    file_save = open( ruta_1, 'w' )
    file_name = open( ruta_2, 'r' )

    #Nombre del player
    player_name = file_name.readlines()  [0]

    #1 Guarde si existe algun guardado
    file_save.write('True\n\n')

    #3 Guarda el nombre del jugador
    file_save.write(player_name+'\n\n')

    #5 Total time
    file_save.write(f'{total_time_in_game + pygame.time.get_ticks()/1000 - time_to_start}\n\n')

    #7 Numero cantidad restante de Avarts
    file_save.write(f'{len(avatar_list)}\n\n')

    #9 Numero de rook que va
    file_save.write(f'{len(list_rooks_in_game)}\n\n')

    #11 Numero de monedas en el juego
    file_save.write(f'{coins}\n\n')

    #Save de Data
    file_save.close()
    file_name.close()


    #Guardar listas y clases
    # Datos que amerita guardar
    data_4 = open('Data/levels', 'wb')

    data_6 = open('Data/MATRIZ', 'wb')

     #For get data in MATRIZ
    data_MATRIZ = []
    for fila in MATRIZ:
        for cuadrito in fila:
            if cuadrito[0] != 'Vacio':
                ps = cuadrito[0].ps_get()
                if ps > 0:
                    tipo = cuadrito[0].type_get()
                    posicion = cuadrito[0].posicion_get()
                    data_MATRIZ.append([tipo, posicion, ps])
                else:
                    cuadrito[0] = 'Vacio'


    #4 Guarda que nivel en el que quedo el usario
    pickle.dump(levels,data_4)

    #6 Matriz
    pickle.dump(data_MATRIZ, data_6)

    #Sale del juego
    game_over = True
    pygame.quit()
    exit()

#---Funciones para niveles---
def start_config_level_1():
    global one_time_upload_levels, num_rook,list_ramdom_secs
    #Creacion de Avatars segun el nivel que se encuentra
    if  one_time_upload_levels[0]:
        list_ramdom_secs = range(10, 14)

        # Creacion de enemigos
        create_enemy( 50, 1 )

        #Creacion de monedas
        create_new_coins(12)

        #Numero de rook
        num_rook = 1000

        #No ejecuta esto mas de una vez
        one_time_upload_levels[0] = False

def start_config_level_2():
    global one_time_upload_levels,list_ramdom_secs, avart_list, num_rook
    #Creacion de Avatars segun el nivel que se encuentra
    if one_time_upload_levels[1]:
        # Tiempo de apracion de avatar entre 4 8
        list_ramdom_secs = range(4, 8)

       # Creacion de enemigos
        create_enemy( 70, 1 )

        #Creacion de monedas
        create_new_coins( 14 )

        #Numero de rook
        num_rook = 1000

        #No ejecuta esto mas de una vez
        one_time_upload_levels[1] = False

def start_config_level_3():
    global one_time_upload_levels,list_ramdom_secs, avart_list, num_rook
    #Creacion de Avatars segun el nivel que se encuentra
    if one_time_upload_levels[2]:
        # Tiempo de apracion de avatar entre 1 3
        list_ramdom_secs = range(1, 3)

        # Creacion de enemigos
        create_enemy( 120, 1 )

        # Creacion de monedas
        create_new_coins(16)

        # Numero de rook
        num_rook = 1000

        # No ejecuta esto mas de una vez
        one_time_upload_levels[2] = False


#---Funciones relacionadas con los avarts y monedas---

def create_enemy (how_much,num):
    global avart_list
    for i in range(how_much):
        avatar = AvartsV0.New_Avart(random.randint(1, 4), num)
        avatar_list.append(avatar)
        num += 1
        all_sprites.add(avatar)

def put_new_enemy(list_ramdom_secs):
    global time_last_time_new_enemy
    num_ramdom = random.choice(list_ramdom_secs)
    if  num_ramdom <= (pygame.time.get_ticks()//1000 - time_last_time_new_enemy)//1:
        time_last_time_new_enemy = pygame.time.get_ticks()//1000
        return put_new_enemy_aux()

def put_new_enemy_aux():

    global avatar_list
    done = False

    for enemy in avatar_list:
        for estado in MATRIZ [8]:
            if estado[0] == 'Vacio' :
                if enemy.posicion_get()[0] == estado[1][0]:
                    estado[0] = enemy
                    avatar_list = avatar_list[1:]
                    list_avarts_in_game.add(enemy)
                    done = True
                    break
            else:
                if estado[0].ps_get() <= 0 :
                    estado[0] =  'Vacio'
                    print('\n Error corregido')


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
                else:
                    if cuadrito[0].ps_get() <= 0:
                        cuadrito[0] = 'Vacio'
                        print('\n Error corregido')




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
                        all_sprites.add(atacking)
                        break
                elif cuadrito[0].type_get() == 'Lenador' or cuadrito[0].type_get() == 'Canival':
                    if i_now - 1 >= 0 and MATRIZ[i_now - 1][j_now][0] != 'Vacio':
                        #print('voy atacar',MATRIZ[i_now - 1][j_now][0].type_get() )
                        if MATRIZ[i_now - 1][j_now][0].type_get() == 'Sand' \
                                or MATRIZ[i_now - 1][j_now][0].type_get() == 'Rock' \
                                or MATRIZ[i_now - 1][j_now][0].type_get() == 'Fire' \
                                or MATRIZ[i_now - 1][j_now][0].type_get() == 'Water' and cuadrito[1][1] ==MATRIZ[i_now - 1][j_now][1][1]:

                            atacking = cuadrito[0].atack(pygame.time.get_ticks())
                            if atacking != '':
                                list_atacks_avart.add(atacking)
                                all_sprites.add(atacking)
                                break
                else:
                    pass
            j_now += 1

        i_now += 1


#---Funciones para el funcionamiento de las monedas---

def create_new_coins(how_much):
    # Conjunto de monedas

    global coin_list
    coin_list = []
    for i in range(how_much):
        coin = CoinsV0.New_Coin(random.randint(1, 3))
        coin_list.append(coin)
        all_sprites.add(coin)

def put_new_coin():
    global time_last_time_new_coin
    global coin_list
    time = random.randint(7,10)
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


#---Funciones para el funcionamiento de los rooks---

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
                else:
                    if  cuadrito[0] != 'Vacio' and cuadrito[0].ps_get() <= 0:
                        cuadrito[0] = 'Vacio'
                        print('\n Error corregido')

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
                        all_sprites.add(atacking)
                else:
                    if cuadrito[0].ps_get() <= 0:
                        cuadrito[0] = 'Vacio'
                        print('\n Error corregido')

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
            else:
                if  cuadrito[0] != "Vacio" and cuadrito[0].ps_get() <= 0:
                    cuadrito[0] = 'Vacio'


#---Funciones para los ataques---

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
    collision_rooks = pygame.sprite.groupcollide(list_rooks_in_game, list_atacks_avart, False, True)
    if collision_rooks != {}:

        attacking = list(collision_rooks.values())[0][0].get_damage()
        list(collision_rooks.values())[0][0].kill()
        rook_victim = list(collision_rooks.keys())[0]

        if rook_victim.life(attacking) == 'i die':
            num = rook_victim.who()

            for fila in MATRIZ:
                for cuadrito in fila:
                    if cuadrito[0] != 'Vacio':
                        if cuadrito[0].who() == num:
                            cuadrito[0].kill()
                            rook_victim.kill()
                            cuadrito[0] = 'Vacio'
                    elif cuadrito[0] == 'Vacio':
                        cuadrito[0] = 'Vacio'


#---Dibuja el los objetos de la matriz---
def draw_objetcs_matriz():
    global MATRIZ
    for fila in MATRIZ:
        for cuadrito in fila:
            object = cuadrito[0]
            if object != 'Vacio':
                object.draw_me(pygame.time.get_ticks())


#---Funcion para quitar el nombre de la lista---
def quit_name(name):
    global player_name
    ruta = "player_name.txt"
    file = open(ruta,"w")
    for line in file:
        if line == player_name:
            line = ""


#---Limpia la matriz y la lista de objetos--
def limpiar_matriz():
    global MATRIZ,matrizcoin
    matrizcoin = [[None],[None],[None],[None],
                  [None],[None],[None],[None],
                  [None],[None],[None],[None],
                  [None],[None],[None]]

    for fila in MATRIZ:
        for cuadrtito in fila:
            cuadrtito[0] = 'Vacio'
    for sprite in all_sprites:
        sprite.kill()

#---Fin del juego--
def you_lost_game():
    global MATRIZ, game_over
    for enemy_false in MATRIZ[0]:

        if enemy_false[0] != 'Vacio':

            if enemy_false[0].type_get() == 'Arquero' or  enemy_false[0].type_get() == 'Escudero' or enemy_false[0].type_get() == 'Canival' or enemy_false[0].type_get()=='Lenador':

                game_over = True
                import GameV0
                
                limpiar_matriz()
                GameV0.start()

# ------------------------------- Pantalla de inicio del menu del juego ------------------------------- #


def juego():
    global MATRIZ, levels, quit_rook_var

    global game_over, shop_open

    global avatar_list, coins, coin_list



    shop_open = True
    game_over = False
    quit_rook_var = False




    # Importa imagenes del escenario
    matriz_0_dibujo = pygame.image.load('resource/matriz_0.png').convert()
    #matriz  1
    #matriz 2
    #matriz 3
    image_save = pygame.image.load('resource/save.jpg').convert()
    image_save = pygame.transform.scale(image_save, [200, 100])
    image_save.set_colorkey(white)
    save_button = pygame.Rect(775, 250, 200, 100)

    # botones tienda
    sand_button = pygame.Rect(0, 500, 100, 80)
    rock_button = pygame.Rect(0, 580, 100, 80)
    fire_button = pygame.Rect(0, 660, 100, 80)
    water_button =pygame.Rect(0, 740, 100, 80)
    quit_button = pygame.Rect(900, 500, 100, 80)


    # Cosas que necesita rooks
    tipo = 0


    #Revisa si hay una partida por cargar
    login()


    while not game_over:

        #Fin del juego
        you_lost_game()

        #Eventos
        for event in pygame.event.get():

            #Salida abruta del juego
            if event.type == pygame.QUIT:
                game_over=True
                pygame.quit()
                exit()

            #Presionar 'Botones' o 'Quitar Rooks'
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

                elif not shop_open:
                    rook_posicion(tipo,pygame.mouse.get_pos())

                #Si presiona el boton de guardar

                if save_button.collidepoint(event.pos):
                    save()


        # Primer Nivel
        if levels[0]:
            screen.fill(white)

            pygame.draw.rect(screen, brown, sand_button)
            pygame.draw.rect(screen, lightgreen, rock_button)
            pygame.draw.rect(screen, green, fire_button)
            pygame.draw.rect(screen, purple, water_button)
            pygame.draw.rect(screen, darkpurple, quit_button)

            pygame.draw.rect(screen, green, save_button )
            screen.blit(image_save,[775,250])
            text(str(coins), font2, brown, screen, 100, 50)
            text('Nivel 1', font2, brown, screen, 100, 200)

            #Pone la cantidad de enemigo y monedas en este nivel
            start_config_level_1()

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

            # Logiga para ganar
            if len(avatar_list) == 0 and len(list_avarts_in_game) == 0 :
                levels[0] = False
                limpiar_matriz()


        #Segundo Nivel
        elif levels[1]:
            screen.fill(purple)

            pygame.draw.rect(screen, brown, sand_button)
            pygame.draw.rect(screen, lightgreen, rock_button)
            pygame.draw.rect(screen, green, fire_button)
            pygame.draw.rect(screen, purple, water_button)
            pygame.draw.rect(screen, darkpurple, quit_button)
            text(str(coins), font2, brown, screen, 100, 50)
            text('Nivel 2', font2, brown, screen, 100, 200)


            pygame.draw.rect(screen, white, save_button )
            screen.blit(image_save, [775, 250])


            #Pone la cantidad de enemigo en este nivel
            start_config_level_2()

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

            # Logiga para ganar
            if len(avatar_list) == 0 and len(list_avarts_in_game) == 0 :
                levels[1] = False
                limpiar_matriz()


        # Tercer Nivel
        elif levels[2]:
            screen.fill(darkpurple)

            pygame.draw.rect(screen, brown, sand_button)
            pygame.draw.rect(screen, lightgreen, rock_button)
            pygame.draw.rect(screen, green, fire_button)
            pygame.draw.rect(screen, purple, water_button)
            pygame.draw.rect(screen, darkpurple, quit_button)
            text(str(coins), font2, brown, screen, 100, 50)
            text('Nivel 3', font2, brown, screen, 100, 200)

            screen.blit(image_save, [775, 250])

            # Pone la cantidad de enemigo en este nivel
            start_config_level_3()

            # Revisa las colisiones
            atacks_colsion_check_avart()
            atacks_colsion_check_rook()

            screen.blit(matriz_0_dibujo, [250, 0])
            draw_objetcs_matriz()

            # Parte funcional para que disparen los rooks
            atacks_rooks()
            list_atacks_rooks.draw(screen)
            # atacks_move()

            # Parte funcional para que disparen los avatars
            atacks_avarts()
            list_atacks_avart.draw(screen)
            atacks_move()
            # Parte funcional avatrs
            put_new_enemy(list_ramdom_secs)
            move_enemy()

            # Parte funcional coins
            put_new_coin()
            draw_coins()
            kill_coins()

            # Logiga para ganar
            if len(avatar_list) == 0 and len(list_avarts_in_game) == 0:
                levels[2] = False
                limpiar_matriz()

        else:
            game_over = True
            import GameV0
            limpiar_matriz()
            GameV0.start()
        clock.tick(60)
        pygame.display.flip()

juego()
