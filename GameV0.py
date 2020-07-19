import pygame, sys, random, pickle
from Objetos import AvartsV0
from Objetos import CoinsV0
from Objetos import RooksV0
from Objetos import Texto_hg
from Objetos import Animacion

# -------------------------------------------- Colores -------------------------------------------- #

dark = (34,32,53)
darkpurple = (87,82,103)
purple = (210, 149, 222)
lightgreen = (160,255,227)
green = (101,220,152)
brown = (141,137,128)
white = (255, 255, 255)
black = (0, 0, 0)
cian = (35, 201, 17)
blue_neo = (13, 0, 65)
# -------------------------------------------- Inicializar -------------------------------------------- #
pygame.init()
pygame.font.init()
pygame.display.set_caption("Avatar vs Rooks")
size = (1000, 800)

screen = pygame.display.set_mode(size)

font = pygame.font.SysFont("Times New Roman", 50)
font2 = pygame.font.SysFont("Times New Roman", 30)
font3 = pygame.font.SysFont("Times New Roman", 20)
font4 = pygame.font.SysFont("Castellar", 70)
font5 = pygame.font.SysFont("Castellar", 45)
clock = pygame.time.Clock()

# ----------------------------------------- Variables globales ----------------------------------------- #
global player_name, list_config

player_name = ""

#Lista de nombre
list_name = pygame.sprite.Group()

# Lista de objetos en el juego
list_atacks_avart = pygame.sprite.Group()

list_atacks_rooks = pygame.sprite.Group()

list_avarts_in_game = pygame.sprite.Group()

list_rooks_in_game = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

# --------------------------------------------- Clases General ---------------------------------------------- #

# --------------------------------------------- Funciones ---------------------------------------------- #
# General-
def text (text, font, color, surface, x , y):
    txtobj = font.render(text, 1, color)
    txtrect = txtobj.get_rect()
    txtrect.center = (x, y)
    surface.blit(txtobj, txtrect)

# --------------------------------------funciones de ventana nuevo nombre --------------------------------------

# ------validacion si el usuario guardo
def validation (name):
    ruta = "Data/player_name.txt"
    file = open(ruta, "r")
    file.close()
    save_name(name)

#       Funcion de guardado en un .txt
def save_name(name):
    global player_name
    player_name = name
    ruta = "Data/player_name.txt"
    file = open(ruta, "w")
    file.write(player_name)
    file.close()



#--------------------------------------funciones de Ventana menu--------------------------------------
# ---Funcion que lee la configuracion del usuario

def read_config():
    global list_config
    list_config = []
    ruta = ("configuracion.txt")
    file = open(ruta, "r")
    sprite = []
    cont = 0
    for line in file:
        if cont == 2:
            list_config.append(sprite)
            sprite = []
            line = int(line)
            sprite.append(line)
            cont = 1
        else:
            cont += 1
            line = int(line)
            sprite.append(line)
    list_config.append(sprite)
    print(list_config)
    file.close()



#--------------------------------------funciones de Ventana configuracion--------------------------------------
# ---Funcion para guardar configuracion en un .txt

def save_config (final_config):
    global save
    save = None
    ruta = "configuracion.txt"
    file = open(ruta, "w")
    for value in final_config:
        value_int = int(value)
        print(value_int)
        if isinstance(value_int, int) and 1 <= value_int <= 6:
            file.write(value)
            file.write('\n')
            save = True
        else:
            save = False
    file.close()


#--------------------------------------funciones de Ventana configuracion--------------------------------------
# ---Funcion para guardar configuracion en un .txt
def create_texto_hg_list():
    #Archivo para aceder la informacion de quien gano
    file_hg_r = open('Data/high_score', 'rb')

    #Carga la lista
    list_hg = pickle.load(file_hg_r)

    #Cierra el archivo
    file_hg_r.close()

    # Logica para poner el texto
    y_pos = 210
    counter = 0
    for texts in list_hg:
        txt = Texto_hg.Texto_hg_cs( texts, font3, cian, screen, 220, y_pos , counter )
        y_pos += 40
        counter += 1
        list_name.add(txt)

def draw_texts_hg_list():
    for texts in list_name:
        texts.draw_me()

def texto_move_hg_list(down_up):
    firt_name = list_name.sprites()[0]
    last_name= list_name.sprites()[len(list_name)-1]

    if down_up  == 'down' and last_name.posicion_get()[1] >= 500:
        for texts in list_name :
            texts.update(-40)
    elif  down_up == 'up' and firt_name.posicion_get()[1] <= 180:
        for texts in list_name:
            texts.update(40)






        #--------------------------------------funciones de ventana juego--------------------------------------

def borrar_lista():
    for texts in list_name:
        texts.kill()
    list_name.empty()

# ---Logica para el guardado

def login():
    # Rutas y Archivos que necesita
    ruta_1 = "Data/game_save.txt"
    ruta_2 = "Data/player_name.txt"
    file_save = open(ruta_1, 'r')
    file_name = open(ruta_2, 'r')

    data_4 = open('Data/levels', 'rb')
    data_5 = open('Data/MATRIZ', 'rb')

    # 1 Resiva si Existe una partida cargada
    boolean_save = file_save.readlines()[0]
    boolean_save = boolean_save[:len(boolean_save) - 1]

    # 3 Get the last player who save
    file_save.seek(0)
    player_save = file_save.readlines()[2]
    player_save = player_save[:len(player_save) - 1]

    # 2 Nombre del player
    player_name = file_name.readlines()[0]

    if bool(boolean_save) and player_name == player_save:
        # 4 Logica para cargar niveles
        load_aux_1(pickle.load(data_4))

        # 5 Poner el tiempo total del juego
        file_save.seek(0)
        line_5 = file_save.readlines()[4]
        line_5 = line_5[:len(line_5) - 1]
        load_aux_2(float(line_5))

        # 6 logica para poner en matriz los elementos, volver a llamar a all_avarts_in_game, all_rooks_in_game, coin_list y all_sprites
        data_MATRIZ = pickle.load(data_5)

        # 7 numero de avarts que quedaban por poner
        file_save.seek(0)
        line_7 = file_save.readlines()[6]
        line_7 = line_7[:len(line_7) - 1]

        # 9 numero de rook por el cual iba
        file_save.seek(0)
        line_9 = file_save.readlines()[8]
        line_9 = line_9[:len(line_9) - 1]

        load_aux_3(data_MATRIZ, int(line_7), int(line_9))

        # linea 11 de monedas en el juego
        file_save.seek(0)
        line_11 = file_save.readlines()[10]
        line_11 = line_11[:len(line_11) - 1]
        load_aux_4(int(line_11))

def load_aux_1(lista):
    global one_time_upload_levels, levels, list_ramdom_secs, num_ramdom

    if lista[0]:
        levels = [True, True, True]
        one_time_upload_levels = [False, True, True]
        list_ramdom_secs = range(3, 10)  # Ahorita se quita
        num_ramdom = random.choice(list_ramdom_secs)
    elif lista[1]:
        levels = [False, True, True]
        one_time_upload_levels = [False, False, True]
        list_ramdom_secs = range(2, 8)  # Ahorita se quita
        num_ramdom = random.choice(list_ramdom_secs)
    else:
        levels = [False, False, True]
        one_time_upload_levels = [False, False, False]
        list_ramdom_secs = range(1, 3)  # Ahorita se quita
        num_ramdom = random.choice(list_ramdom_secs)

def load_aux_2(num):
    global total_time_in_game
    total_time_in_game += num

def load_aux_3(m, num1, num2):
    global MATRIZ, num_rook, levels
    # Pone el numero de rook
    num_rook = num2 + 1000
    num2_aux = num2

    # Revisa cuantos avarts quedan en el juego
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
                name_tipo = elements[0]

                # Logica para saber que tipo era
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

                # Logica que posiciona si es avart
                if 1 <= tipo <= 4 and (cuadrito[1][0] == elements[1][0]) and (
                        cuadrito[1][1] == elements[1][1] + 20) and num1_aux != 0:
                    avart = AvartsV0.New_Avart(tipo, num1_aux, white, size, list_config)
                    num1_aux -= 1
                    avart.set_guardado(elements[1], elements[2])
                    list_avarts_in_game.add(avart)
                    all_sprites.add(avart)
                    cuadrito[0] = avart

                # Logica para ponersi es rook
                elif 5 <= tipo <= 8 and (cuadrito[1][0] == elements[1][0]) and (
                        cuadrito[1][1] == elements[1][1]) and num2_aux != 1000:
                    rook = RooksV0.New_Rook(tipo, cuadrito[1], num2_aux, white, list_config)
                    num2_aux -= 1
                    rook.set_guardado(elements[2])
                    list_rooks_in_game.add(rook)
                    all_sprites.add(rook)
                    cuadrito[0] = rook

                # Si el cuadrito no tiene la misma posicion
                else:
                    pass

    # Crea los avarts restantes en avart list
    create_enemy(num1, num_avart)

def load_aux_4(num):
    global coins
    create_new_coins(12)
    coins = num

def save():
    global MATRIZ, one_time_upload_levels, total_time_in_game, time_to_start, avatar_list, coins, game_over

    # Rutas y Archivos que necesita
    ruta_1 = "Data/game_save.txt"
    ruta_2 = "Data/player_name.txt"
    file_save = open(ruta_1, 'w')
    file_name = open(ruta_2, 'r')

    # Nombre del player
    player_name = file_name.readlines()[0]

    # 1 Guarde si existe algun guardado
    file_save.write('True\n\n')

    # 3 Guarda el nombre del jugador
    file_save.write(player_name + '\n\n')

    # 5 Total time
    file_save.write(f'{total_time_in_game + pygame.time.get_ticks() / 1000 - time_to_start}\n\n')

    # 7 Numero cantidad restante de Avarts
    file_save.write(f'{len(avatar_list)}\n\n')

    # 9 Numero de rook que va
    file_save.write(f'{len(list_rooks_in_game)}\n\n')

    # 11 Numero de monedas en el juego
    file_save.write(f'{coins}\n\n')

    # Save de Data
    file_save.close()
    file_name.close()

    # Guardar listas y clases
    # Datos que amerita guardar
    data_4 = open('Data/levels', 'wb')

    data_6 = open('Data/MATRIZ', 'wb')

    # For get data in MATRIZ
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

    # 4 Guarda que nivel en el que quedo el usario
    pickle.dump(levels, data_4)

    # 6 Matriz
    pickle.dump(data_MATRIZ, data_6)

    # Sale del juego
    game_over = True
    pygame.quit()
    exit()


# ---Funciones para niveles

def start_config_level_1():
    global one_time_upload_levels, num_rook, list_ramdom_secs ,num_ramdom
    # Creacion de Avatars segun el nivel que se encuentra
    if one_time_upload_levels[0]:
        list_ramdom_secs = range(3, 10)
        num_ramdom = random.choice(list_ramdom_secs)

        # Creacion de enemigos
        create_enemy(50, 1)

        # Creacion de monedas
        create_new_coins(12)

        # Numero de rook
        num_rook = 1000

        # No ejecuta esto mas de una vez
        one_time_upload_levels[0] = False

def start_config_level_2():
    global one_time_upload_levels, list_ramdom_secs, avart_list, num_rook
    # Creacion de Avatars segun el nivel que se encuentra
    if one_time_upload_levels[1]:
        # Tiempo de apracion de avatar entre 4 8
        list_ramdom_secs = range(2, 8)
        num_ramdom = random.choice(list_ramdom_secs)

        # Creacion de enemigos
        create_enemy(70, 1)

        # Creacion de monedas
        create_new_coins(14)

        # Numero de rook
        num_rook = 1000

        # No ejecuta esto mas de una vez
        one_time_upload_levels[1] = False

def start_config_level_3():
    global one_time_upload_levels, list_ramdom_secs, avart_list, num_rook
    # Creacion de Avatars segun el nivel que se encuentra
    if one_time_upload_levels[2]:
        # Tiempo de apracion de avatar entre 1 3
        list_ramdom_secs = range(1, 3)
        num_ramdom = random.choice(list_ramdom_secs)

        # Creacion de enemigos
        create_enemy(120, 1)

        # Creacion de monedas
        create_new_coins(16)

        # Numero de rook
        num_rook = 1000

        # No ejecuta esto mas de una vez
        one_time_upload_levels[2] = False


# ---Funciones relacionadas con los avarts y monedas

def create_enemy(how_much, num):
    global avart_list
    for i in range(how_much):
        avatar = AvartsV0.New_Avart(random.randint(1, 4), num, white, size, list_config)
        avatar_list.append(avatar)
        num += 1
        all_sprites.add(avatar)

def put_new_enemy(list_ramdom_secs):
    global time_last_time_new_enemy , num_ramdom
    if num_ramdom <= (pygame.time.get_ticks() // 1000 - time_last_time_new_enemy) // 1:
        num_ramdom = random.choice(list_ramdom_secs)
        time_last_time_new_enemy = pygame.time.get_ticks() // 1000
        return put_new_enemy_aux()

def put_new_enemy_aux():
    global avatar_list
    done = False
    for enemy in avatar_list:
        for estado in MATRIZ[8]:
            if estado[0] == 'Vacio':
                if enemy.posicion_get()[0] == estado[1][0]:
                    estado[0] = enemy
                    avatar_list = avatar_list[1:]
                    list_avarts_in_game.add(enemy)
                    done = True
                    break
            else:
                if estado[0].ps_get() <= 0:
                    estado[0] = 'Vacio'
                    print('\n Error corregido')
        if done:
            break

def move_enemy():
    global MATRIZ, game_over
    i_now = 0
    for fila in MATRIZ:
        j_now = 0
        for cuadrito in fila:
            # Revisa si hay personaje
            if cuadrito[0] != 'Vacio':
                # Revisa si
                if cuadrito[0].type_get() == 'Arquero' or cuadrito[0].type_get() == 'Escudero' \
                        or cuadrito[0].type_get() == 'Lenador' or cuadrito[0].type_get() == 'Canival':
                    # Revisa si es posible el cambio
                    if i_now - 1 >= 0 and MATRIZ[i_now - 1][j_now][0] == 'Vacio':
                        if cuadrito[0].update(pygame.time.get_ticks()):
                            MATRIZ[i_now - 1][j_now][0] = cuadrito[0]
                            cuadrito[0] = 'Vacio'
                else:
                    if cuadrito[0].ps_get() <= 0:
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
                if cuadrito[0].type_get() == 'Arquero' or cuadrito[0].type_get() == 'Escudero' and atacks_avarts_check(cuadrito[1][0]) :
                    atacking = cuadrito[0].atack(pygame.time.get_ticks())
                    if atacking != '':
                        list_atacks_avart.add(atacking)
                        all_sprites.add(atacking)
                        break
                elif cuadrito[0].type_get() == 'Lenador' or cuadrito[0].type_get() == 'Canival':
                    if i_now - 1 >= 0 and MATRIZ[i_now - 1][j_now][0] != 'Vacio':
                        if MATRIZ[i_now - 1][j_now][0].type_get() == 'Sand' \
                                or MATRIZ[i_now - 1][j_now][0].type_get() == 'Rock' \
                                or MATRIZ[i_now - 1][j_now][0].type_get() == 'Fire' \
                                or MATRIZ[i_now - 1][j_now][0].type_get() == 'Water' and cuadrito[1][1] == \
                                MATRIZ[i_now - 1][j_now][1][1]:
                            atacking = cuadrito[0].atack(pygame.time.get_ticks())
                            if atacking != '':
                                list_atacks_avart.add(atacking)
                                all_sprites.add(atacking)
                                break
                else:
                    pass
            j_now += 1
        i_now += 1

def atacks_avarts_check(pos_x):
    global MATRIZ
    result = False
    for fila in MATRIZ:
        for cuadrito in fila:
            if cuadrito[1][0] == pos_x:
                if cuadrito[0] != 'Vacio':
                    if cuadrito[0].type_get() == 'Sand' or cuadrito[0].type_get() == 'Rock' \
                    or cuadrito[0].type_get() == 'Fire' or cuadrito[0].type_get() == 'Water':
                        result = True
                        break
        if result:
            break
    return result
# ---Funciones para el funcionamiento de las monedas---

def create_new_coins(how_much):
    # Conjunto de monedas
    global coin_list
    coin_list = []
    for i in range(how_much):
        coin = CoinsV0.New_Coin(random.randint(1, 3), black)
        coin_list.append(coin)
        all_sprites.add(coin)

def put_new_coin():
    global time_last_time_new_coin
    global coin_list
    time = random.randint(7, 10)
    if time == int(pygame.time.get_ticks() // 1000 - time_last_time_new_coin):
        time_last_time_new_coin = pygame.time.get_ticks() // 1000
        return put_new_coin_aux()

def put_new_coin_aux():
    global matrizcoin, coin_list
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

def draw_coins():
    global matrizcoin
    for moneda in matrizcoin:
        coins = moneda[0]
        if coins != None:
            coins.update(screen)

def kill_coins():
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
            if coin_pos[0] <= mouse_pos[0] <= coin_pos[0] + 50 and mouse_click[0] == 1 and coin_pos[1] <= mouse_pos[
                1] <= coin_pos[1] + 50:
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


# ---Funciones para el funcionamiento de los rooks---

def rook_posicion(tipo, mouse_pos):
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
    put_new_rook([tipo, set, [rectX, rectY]])

def put_new_rook(lists):
    global MATRIZ, shop_open
    if not lists[1]:
        for fila in MATRIZ:
            for cuadrito in fila:
                if cuadrito[0] == 'Vacio' and cuadrito[1] == lists[2]:
                    cuadrito[0] = new_rook(lists[0], lists[2])
                    list_rooks_in_game.add(cuadrito[0])
                    all_sprites.add(cuadrito[0])
                    shop_open = True
                else:
                    if cuadrito[0] != 'Vacio' and cuadrito[0].ps_get() <= 0:
                        cuadrito[0] = 'Vacio'

def new_rook(tipo, pos):
    global num_rook
    rook = []
    if tipo == 5:
        rook = RooksV0.New_Rook(tipo, pos, num_rook, white, list_config)
    if tipo == 6:
        rook = RooksV0.New_Rook(tipo, pos, num_rook, white, list_config)
    if tipo == 7:
        rook = RooksV0.New_Rook(tipo, pos, num_rook, white, list_config)
    if tipo == 8:
        rook = RooksV0.New_Rook(tipo, pos, num_rook, white, list_config)
    num_rook += 1
    return rook

def atacks_rooks():
    global MATRIZ
    for fila in MATRIZ:
        for cuadrito in fila:
            if cuadrito[0] != 'Vacio':
                if not (cuadrito[0].type_get() == 'Arquero' or cuadrito[0].type_get() == 'Escudero'
                        or cuadrito[0].type_get() == 'Lenador' or cuadrito[0].type_get() == 'Canival') and atacks_rooks_check(cuadrito[1][0]):
                    # Ataque
                    atacking = cuadrito[0].atack(pygame.time.get_ticks(), list_config)
                    if atacking != '':
                        list_atacks_rooks.add(atacking)
                        all_sprites.add(atacking)
                else:
                    if cuadrito[0].ps_get() <= 0:
                        cuadrito[0] = 'Vacio'

def atacks_rooks_check(pos_x):
    global MATRIZ
    result = False
    for fila in MATRIZ:
        for cuadrito in fila:
            if cuadrito[1][0] == pos_x:
                if cuadrito[0] !='Vacio':
                     if cuadrito[0].type_get() == 'Arquero' or cuadrito[0].type_get() == 'Escudero'  \
                        or cuadrito[0].type_get() == 'Lenador' or cuadrito[0].type_get() == 'Canival':
                        result = True
                        break
        if result:
            break
    return result

def click_posicion(mouse_pos):
    # Identifica la posicion del rook a quitar

    # primer fila

    if 250 < mouse_pos[0] < 350 and 0 < mouse_pos[1] < 90:
        rectX = 250
        rectY = 0
    elif 350 < mouse_pos[0] < 450 and 0 < mouse_pos[1] < 90:
        rectX = 350
        rectY = 0
    elif 450 < mouse_pos[0] < 550 and 0 < mouse_pos[1] < 90:
        rectX = 450
        rectY = 0
    elif 550 < mouse_pos[0] < 650 and 0 < mouse_pos[1] < 90:
        rectX = 550
        rectY = 0
    elif 650 < mouse_pos[0] < 750 and 0 < mouse_pos[1] < 90:
        rectX = 650
        rectY = 0
    # segunda fila
    elif 250 < mouse_pos[0] < 350 and 90 < mouse_pos[1] < 180:
        rectX = 250
        rectY = 90
    elif 350 < mouse_pos[0] < 450 and 90 < mouse_pos[1] < 180:
        rectX = 350
        rectY = 90
    elif 450 < mouse_pos[0] < 550 and 90 < mouse_pos[1] < 180:
        rectX = 450
        rectY = 90
    elif 550 < mouse_pos[0] < 650 and 90 < mouse_pos[1] < 180:
        rectX = 550
        rectY = 90
    elif 650 < mouse_pos[0] < 750 and 90 < mouse_pos[1] < 180:
        rectX = 650
        rectY = 90

    # tercera fila

    elif 250 < mouse_pos[0] < 350 and 180 < mouse_pos[1] < 270:
        rectX = 250
        rectY = 180
    elif 350 < mouse_pos[0] < 450 and 180 < mouse_pos[1] < 270:
        rectX = 350
        rectY = 180
    elif 450 < mouse_pos[0] < 550 and 180 < mouse_pos[1] < 270:
        rectX = 450
        rectY = 180
    elif 550 < mouse_pos[0] < 650 and 180 < mouse_pos[1] < 270:
        rectX = 550
        rectY = 180

    elif 650 < mouse_pos[0] < 750 and 180 < mouse_pos[1] < 270:
        rectX = 650
        rectY = 180

    # cuarta fila

    elif 250 < mouse_pos[0] < 350 and 270 < mouse_pos[1] < 360:
        rectX = 250
        rectY = 270
    elif 350 < mouse_pos[0] < 450 and 270 < mouse_pos[1] < 360:
        rectX = 350
        rectY = 270
    elif 450 < mouse_pos[0] < 550 and 270 < mouse_pos[1] < 360:
        rectX = 450
        rectY = 270
    elif 550 < mouse_pos[0] < 650 and 270 < mouse_pos[1] < 360:
        rectX = 550
        rectY = 270
    elif 650 < mouse_pos[0] < 750 and 270 < mouse_pos[1] < 360:
        rectX = 650
        rectY = 270

        # quinta fila

    elif 250 < mouse_pos[0] < 350 and 360 < mouse_pos[1] < 450:
        rectX = 250
        rectY = 360
    elif 350 < mouse_pos[0] < 450 and 360 < mouse_pos[1] < 450:
        rectX = 350
        rectY = 360
    elif 450 < mouse_pos[0] < 550 and 360 < mouse_pos[1] < 450:
        rectX = 450
        rectY = 360
    elif 550 < mouse_pos[0] < 650 and 360 < mouse_pos[1] < 450:
        rectX = 550
        rectY = 360
    elif 650 < mouse_pos[0] < 750 and 360 < mouse_pos[1] < 450:
        rectX = 650
        rectY = 360

        # sexta fila

    elif 250 < mouse_pos[0] < 350 and 450 < mouse_pos[1] < 540:
        rectX = 250
        rectY = 450
    elif 350 < mouse_pos[0] < 450 and 450 < mouse_pos[1] < 540:
        rectX = 350
        rectY = 450

    elif 450 < mouse_pos[0] < 550 and 450 < mouse_pos[1] < 540:
        rectX = 450
        rectY = 450
    elif 550 < mouse_pos[0] < 650 and 450 < mouse_pos[1] < 540:
        rectX = 550
        rectY = 450
    elif 650 < mouse_pos[0] < 750 and 450 < mouse_pos[1] < 540:
        rectX = 650
        rectY = 450

        # septima fila

    elif 250 < mouse_pos[0] < 350 and 540 < mouse_pos[1] < 630:
        rectX = 250
        rectY = 540
    elif 350 < mouse_pos[0] < 450 and 540 < mouse_pos[1] < 630:
        rectX = 350
        rectY = 540
    elif 450 < mouse_pos[0] < 550 and 540 < mouse_pos[1] < 630:
        rectX = 450
        rectY = 540
    elif 550 < mouse_pos[0] < 650 and 540 < mouse_pos[1] < 630:
        rectX = 550
        rectY = 540
    elif 650 < mouse_pos[0] < 750 and 540 < mouse_pos[1] < 630:
        rectX = 650
        rectY = 540

        # octava fila

    elif 250 < mouse_pos[0] < 350 and 630 < mouse_pos[1] < 720:
        rectX = 250
        rectY = 630
    elif 350 < mouse_pos[0] < 450 and 630 < mouse_pos[1] < 720:
        rectX = 350
        rectY = 630
    elif 450 < mouse_pos[0] < 550 and 630 < mouse_pos[1] < 720:
        rectX = 450
        rectY = 630
    elif 550 < mouse_pos[0] < 650 and 630 < mouse_pos[1] < 720:
        rectX = 550
        rectY = 630
    elif 650 < mouse_pos[0] < 750 and 630 < mouse_pos[1] < 720:
        rectX = 650
        rectY = 630

    # novena fila

    elif 250 < mouse_pos[0] < 350 and 720 < mouse_pos[1] < 810:
        rectX = 250
        rectY = 720
    elif 350 < mouse_pos[0] < 450 and 720 < mouse_pos[1] < 810:
        rectX = 350
        rectY = 720
    elif 450 < mouse_pos[0] < 550 and 720 < mouse_pos[1] < 810:
        rectX = 450
        rectY = 720
    elif 550 < mouse_pos[0] < 650 and 720 < mouse_pos[1] < 810:
        rectX = 550
        rectY = 720
    elif 650 < mouse_pos[0] < 750 and 720 < mouse_pos[1] < 810:
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
                if cuadrito[0].type_get() == "Sand" or cuadrito[0].type_get() == "Rock" or \
                        cuadrito[0].type_get() == "Fire" or cuadrito[0].type_get() == "Water":
                    cuadrito[0].kill()
                    cuadrito[0] = "Vacio"
                else:
                    print("no se puede eliminar avatar")  # ver como indicar esto
            elif cuadrito[0] == "Vacio":
                pass
            else:
                if cuadrito[0] != "Vacio" and cuadrito[0].ps_get() <= 0:
                    cuadrito[0] = 'Vacio'


# ---Funciones para los ataques

def atacks_move():
    for atacking_rook in list_atacks_rooks:
        atacking_rook.update(size)

    for atacking_avart in list_atacks_avart:
        atacking_avart.update()

def atacks_colsion_check_avart():
    global MATRIZ, coins
    # Logica para avatar impacto
    colisicion_avarts = pygame.sprite.groupcollide(list_avarts_in_game, list_atacks_rooks, False, True)
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
                        if cuadrito[0].who() == num:
                            cuadrito[0].kill()
                            avatar_victimin.kill()
                            cuadrito[0] = 'Vacio'
                    elif cuadrito[0] == 'Vacio':
                        cuadrito[0] = 'Vacio'

def atacks_colsion_check_rook():
    global MATRIZ
    # Logica para avatar impacto
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


# ---Dibuja el los objetos de la matriz

def draw_objetcs_matriz():
    global MATRIZ
    for fila in MATRIZ:
        for cuadrito in fila:
            object = cuadrito[0]
            if object != 'Vacio':
                object.draw_me(pygame.time.get_ticks(), screen)


# ---Funcion para quitar el nombre de la lista

def quit_name(name):
    global player_name
    ruta = "player_name.txt"
    file = open(ruta, "w")
    for line in file:
        if line == player_name:
            line = ""


# ---Limpia la matriz y la lista de objetos
def limpiar_matriz():
    global MATRIZ, matrizcoin
    matrizcoin = [[None], [None], [None], [None],
                  [None], [None], [None], [None],
                  [None], [None], [None], [None],
                  [None], [None], [None]]

    for fila in MATRIZ:
        for cuadrtito in fila:
            cuadrtito[0] = 'Vacio'
    for sprite in all_sprites:
        sprite.kill()


# ---Fin del juego
def you_lost_game():
    global MATRIZ, game_over , levels, one_time_upload_levels , coins
    for enemy_false in MATRIZ[0]:
        if enemy_false[0] != 'Vacio':
            if enemy_false[0].type_get() == 'Arquero' or enemy_false[0].type_get() == 'Escudero' or \
               enemy_false[0].type_get() == 'Canival' or enemy_false[0].type_get() == 'Lenador':

                pygame.time.wait(1000)
                game_over = True
                limpiar_matriz()
                levels = [True, True, True]
                one_time_upload_levels = [True, True, True]
                coins = 100

                game_over_ani()

def high_score_save():
    time = round((total_time_in_game-time_to_start+pygame.time.get_ticks()/1000), 2)
    #Archivos
    file_name = open ('Data/player_name.txt', 'r')
    file_hg_r = open('Data/high_score','rb')

    #Variables de los archivos
    names_player =   file_name.readlines()[0]
    list_hg = pickle.load(file_hg_r)

    #Cierres de Archivos
    file_name.close()
    file_hg_r.close()

    #Variables axuliares
    mismo = False

    #Logica para comprobar si hay otro nombre igual
    c = 0
    for item in list_hg:
        if item [1] == names_player:
            list_hg[c] = ( time, names_player )
            mismo = True
            break
        c+=1



    #Revisa si tiene agregar un elmento o no
    if not mismo:
        print('No cambio\n\n')
        #Agrega la nueva tupla
        list_hg.append( ( time, names_player ) )

    #Ordena la lista
    new_list_hg = sorted(list_hg, key=lambda times: times[0] )


    # Modo escritura de el archivo
    file_hg_w = open('Data/high_score', 'wb')

    #Agrega la nueva lista
    pickle.dump( new_list_hg, file_hg_w )

    file_hg_r.close()



# --------------------------------------------- Ventanas --------------------------------------------- #

# Ventana win

def win_ani():

    sprite_win = Animacion.animacion('resource/win.png', (200, 200), 96, 96, 4)
    sprite_win2 = Animacion.animacion('resource/win.png', (800, 175), 96, 96, 4)
    sprite_win3 = Animacion.animacion('resource/win.png', (600, 400), 96, 96, 4)
    sprite_win4 = Animacion.animacion('resource/win.png', (150, 500), 96, 96, 4)
    sprite_win5 = Animacion.animacion('resource/win.png', (850, 675), 96, 96, 4)
    sprite_win6 = Animacion.animacion('resource/win.png', (220, 700), 96, 96, 4)

    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_2:
                    run = False
                    sprite_win.kill()
                    sprite_win2.kill()
                    sprite_win3.kill()
                    start()

        screen.fill(dark)  # color la ventana
        sprite_win.update(screen)
        sprite_win2.update(screen)
        sprite_win3.update(screen)
        sprite_win4.update(screen)
        sprite_win5.update(screen)
        sprite_win6.update(screen)

        text("Felicidades", font4, darkpurple, screen, 500, 100)
        text("has ganado", font5, darkpurple, screen, 500, 200)
        text("Presiona una tecla 2 para iniciar", font3, brown, screen, 505, 605)

        pygame.display.flip()
        clock.tick(6)

# Ventana game over
def game_over_ani():

    sprite = Animacion.animacion('resource/gameover.png', (500,450), 99, 96, 14)

    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    run = False
                    sprite.kill()
                    start()


        screen.fill(dark)  # color la ventana
        sprite.update(screen)
        text("Game Over", font4, darkpurple, screen, 500, 300)
        text("Presiona una tecla 1 para iniciar", font3, brown, screen, 500, 600)

        pygame.display.flip()
        clock.tick(10)

# Ventana configuracion
def config():
    screen.fill(dark) # color de la ventana

    # ------------------------------------ Imagenes ------------------------------------ #

    music_on = pygame.image.load("resource/music_on.png").convert()
    music_on.set_colorkey(white)
    music_off = pygame.image.load("resource/music_off.png").convert()
    music_off.set_colorkey(white)
    flechador_raw = pygame.image.load("resource/avatar_flechador.png").convert()
    flechador_raw.set_colorkey(white)
    flechadorimg = pygame.transform.scale(flechador_raw, (80, 80))
    escudero_raw = pygame.image.load("resource/avatar_escudero.png").convert()
    escudero_raw.set_colorkey(white)
    escuderoimg = pygame.transform.scale(escudero_raw, (80, 80))
    leñador_raw = pygame.image.load("resource/avatar_lenador.png").convert()
    leñador_raw.set_colorkey(white)
    leñadorimg = pygame.transform.scale(leñador_raw, (80, 80))
    carnival_raw = pygame.image.load("resource/avatar_canival.png").convert()
    carnival_raw.set_colorkey(white)
    carnivalimg = pygame.transform.scale(carnival_raw, (80, 80))

    sand_raw = pygame.image.load("resource/rook_sand.png").convert()
    sand_raw.set_colorkey(white)
    sandimg = pygame.transform.scale(sand_raw, (80, 80))
    rock_raw = pygame.image.load("resource/rook_rock.png").convert()
    rock_raw.set_colorkey(white)
    rockimg = pygame.transform.scale(rock_raw, (80, 80))
    fire_raw = pygame.image.load("resource/rook_fire.png").convert()
    fire_raw.set_colorkey(white)
    fireimg = pygame.transform.scale(fire_raw, (80, 80))
    water_raw = pygame.image.load("resource/rook_water.png").convert()
    water_raw.set_colorkey(white)
    waterimg = pygame.transform.scale(water_raw, (80, 80))

    # ------------------------------------ Dibujos ------------------------------------ #

    saveconfig_button = pygame.Rect(380, 650, 220, 50)
    avatar = pygame.Rect(0, 40, 500, 70)
    rook = pygame.Rect(0, 340, 500, 70)
    rook_box = pygame.Rect(70, 590, 860, 50)

    # Avatars
    flechador = pygame.Rect(70, 130, 200, 200)
    escudero = pygame.Rect(290, 130, 200, 200)
    leñador = pygame.Rect(510, 130, 200, 200)
    carnival = pygame.Rect(730, 130, 200, 200)
    # Rooks
    sand = pygame.Rect(70, 430, 200, 150)
    rock = pygame.Rect(290, 430, 200, 150)
    fire = pygame.Rect(510, 430, 200, 150)
    water = pygame.Rect(730, 430, 200, 150)

    # Entry box speed
    entrybox_f = pygame.Rect(170, 250, 90, 25)
    entrybox_e = pygame.Rect(390, 250, 90, 25)
    entrybox_l = pygame.Rect(610, 250, 90, 25)
    entrybox_c = pygame.Rect(830, 250, 90, 25)

    # Entry box atack
    entrybox_f_at = pygame.Rect(170, 295, 90, 25)
    entrybox_e_at = pygame.Rect(390, 295, 90, 25)
    entrybox_l_at = pygame.Rect(610, 295, 90, 25)
    entrybox_c_at = pygame.Rect(830, 295, 90, 25)
    entrybox_rooks = pygame.Rect(320, 600, 600, 30)

    # Se dibuja rectangulos de titulos o botones
    pygame.draw.rect(screen, green, saveconfig_button)
    pygame.draw.rect(screen, darkpurple, avatar)
    pygame.draw.rect(screen, darkpurple, rook)
    pygame.draw.rect(screen, brown, rook_box)
    # Se dibuja las cartas de los avatars
    pygame.draw.rect(screen, brown, flechador)
    pygame.draw.rect(screen, brown, escudero)
    pygame.draw.rect(screen, brown, leñador)
    pygame.draw.rect(screen, brown, carnival)
    # Se dibuja las cartas de los rooks
    pygame.draw.rect(screen, brown, sand)
    pygame.draw.rect(screen, brown, rock)
    pygame.draw.rect(screen, brown, fire)
    pygame.draw.rect(screen, brown, water)

    # ------------------------------------ texto en pantalla ------------------------------------ #
    #   Texto de la entry
    text("Velocidad", font3, dark, screen, flechador.x + 50, flechador.y + 130)
    text("Ataque", font3, dark, screen, flechador.x + 40, flechador.y + 175)
    text("Velocidad", font3, dark, screen, escudero.x + 50, escudero.y + 130)
    text("Ataque", font3, dark, screen, escudero.x + 40, escudero.y + 175)
    text("Velocidad", font3, dark, screen, carnival.x + 50, carnival.y + 130)
    text("Ataque", font3, dark, screen, carnival.x + 40, carnival.y + 175)
    text("Velocidad", font3, dark, screen, carnival.x + 50, carnival.y + 130)
    text("Ataque", font3, dark, screen, carnival.x + 40, carnival.y + 175)
    text("Velocidad", font3, dark, screen, leñador.x + 50, leñador.y + 130)
    text("Ataque", font3, dark, screen, leñador.x + 40, leñador.y + 175)

    #   Texto boton y titulos

    text('Guardar cambios', font2, brown, screen, saveconfig_button.x + 110, saveconfig_button.y + 25)
    text("Avatars", font, purple, screen, avatar.x + 250, avatar.y + 35)
    text("Rooks", font, purple, screen, rook.x + 250, rook.y + 35)
    text("Velocidad de ataque", font3, dark, screen, entrybox_rooks.x - 120, entrybox_rooks.y + 15)

    # Texto nombres
    text("Arquero", font2, purple, screen, flechador.x + 100, flechador.y + 15)
    text("Escudero", font2, purple, screen, escudero.x + 100, escudero.y + 15)
    text("Leñador", font2, purple, screen, leñador.x + 100, leñador.y + 15)
    text("Caníval", font2, purple, screen, carnival.x + 100, carnival.y + 15)
    text("Arena", font2, purple, screen, sand.x + 100, sand.y + 15)
    text("Roca", font2, purple, screen, rock.x + 100, rock.y + 15)
    text("Fuego", font2, purple, screen, fire.x + 100, fire.y + 15)
    text("Agua", font2, purple, screen, water.x + 100, water.y + 15)
    # Variables que activan los entrybox
    #   Velocidad
    active_f = False
    active_e = False
    active_l = False
    active_c = False
    #   Ataque
    active_f_at = False
    active_e_at = False
    active_l_at = False
    active_c_at = False
    active_rook_at = False

    # ------------------------------------ variables de texto ------------------------------------ #
    global speed_f, speed_e, speed_l, speed_c, atack_f, atack_e, atack_l, atack_c, atack_rook
    speed_f = ""
    speed_e = ""
    speed_l = ""
    speed_c = ""
    atack_f = ""
    atack_e = ""
    atack_l = ""
    atack_c = ""
    atack_rook = ""

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if entrybox_f.collidepoint(event.pos):
                    active_f = True
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False
                elif entrybox_e.collidepoint(event.pos):
                    active_f = False
                    active_e = True
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False
                elif entrybox_l.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = True
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False
                elif entrybox_c.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = True
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False

                # activar entry para ataque
                elif entrybox_f_at.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = True
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False
                elif entrybox_e_at.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = True
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False
                elif entrybox_l_at.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = True
                    active_c_at = False
                    active_rook_at = False
                elif entrybox_c_at.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = True
                    active_rook_at = False
                elif entrybox_rooks.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = True
                elif 850 < mouse_pos[0] < 914 and 730 < mouse_pos[1] < 794:
                    pygame.mixer.music.load("resource/song1.wav")
                    pygame.mixer.music.play(loops=-1)
                    print("si funciono")
                elif 930 < mouse_pos[0] < 994 and 730 < mouse_pos[1] < 794:
                    pygame.mixer.music.stop()
                elif saveconfig_button.collidepoint(event.pos):
                    global save
                    save_config(final_config)
                    if save:
                        run = False
                        menu()
                    else:
                        text("Favor introducir valores entre 1 y 6 segundos", font2, green, screen, 500, 750)

                else:
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False
            elif event.type == pygame.KEYDOWN:
                if active_f:
                    if event.key == pygame.K_BACKSPACE:
                        speed_f = speed_f[0:-1]
                    elif event.key == pygame.K_TAB:
                        speed_f = speed_f
                    else:
                        speed_f += event.unicode
                elif active_e:
                    if event.key == pygame.K_BACKSPACE:
                        speed_e = speed_e[0:-1]
                    elif event.key == pygame.K_TAB:
                        speed_e = speed_e

                    else:
                        speed_e += event.unicode
                elif active_l:
                    if event.key == pygame.K_BACKSPACE:
                        speed_l = speed_l[0:-1]
                    elif event.key == pygame.K_TAB:
                        speed_l = speed_l
                    else:
                        speed_l += event.unicode
                elif active_c:
                    if event.key == pygame.K_BACKSPACE:
                        speed_c = speed_c[0:-1]
                    elif event.key == pygame.K_TAB:
                        speed_c = speed_c
                    else:
                        speed_c += event.unicode

                # typing rooks

                elif active_f_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_f = atack_f[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_f = atack_f
                    else:
                        atack_f += event.unicode
                elif active_e_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_e = atack_e[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_e = atack_e
                    else:
                        atack_e += event.unicode
                elif active_l_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_l = atack_l[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_l = atack_l
                    else:
                        atack_l += event.unicode
                elif active_c_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_c = atack_c[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_c = atack_c
                    else:
                        atack_c += event.unicode
                elif active_rook_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_rook = atack_rook[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_rook = atack_rook
                    else:
                        atack_rook += event.unicode

        # Lista que contien todos los segundos
        final_config = [speed_f,atack_f, speed_e, atack_e,
                        speed_l, atack_l, speed_c,atack_c
                        ,atack_rook]

        # Se dibujan iconos de musica
        screen.blit(music_on, (850, 730))
        screen.blit(music_off, (930, 730))
        # Se dibujan avatars
        screen.blit(flechadorimg, (flechador.x + 60, flechador.y + 35))
        screen.blit(escuderoimg, (escudero.x + 60, escudero.y + 35))
        screen.blit(leñadorimg, (leñador.x + 60, leñador.y + 35))
        screen.blit(carnivalimg, (carnival.x + 60, carnival.y + 35))
        # Se dibujan rook
        screen.blit(sandimg, (sand.x + 60, sand.y + 40))
        screen.blit(rockimg, (rock.x + 60, rock.y + 40))
        screen.blit(fireimg, (fire.x + 60, fire.y + 40))
        screen.blit(waterimg, (water.x + 60, water.y + 40))
        # Se dibuja los entry box de speed
        pygame.draw.rect(screen, white, entrybox_f)
        pygame.draw.rect(screen, white, entrybox_e)
        pygame.draw.rect(screen, white, entrybox_l)
        pygame.draw.rect(screen, white, entrybox_c)

        # Se dibuja los entry box de atack
        pygame.draw.rect(screen, white, entrybox_f_at)
        pygame.draw.rect(screen, white, entrybox_e_at)
        pygame.draw.rect(screen, white, entrybox_l_at)
        pygame.draw.rect(screen, white, entrybox_c_at)
        pygame.draw.rect(screen, white, entrybox_rooks)

        # Se dibuja text de speed avatar
        text(speed_f, font3, dark, screen, entrybox_f.x + 45, entrybox_f.y + 12)
        text(speed_e, font3, dark, screen, entrybox_e.x + 45, entrybox_e.y + 12)
        text(speed_l, font3, dark, screen, entrybox_l.x + 45, entrybox_l.y + 12)
        text(speed_c, font3, dark, screen, entrybox_c.x + 45, entrybox_c.y + 12)

        # Se dibuja text de atack avatar
        text(atack_f, font3, dark, screen, entrybox_f_at.x + 45, entrybox_f_at.y + 12)
        text(atack_e, font3, dark, screen, entrybox_e_at.x + 45, entrybox_e_at.y + 12)
        text(atack_l, font3, dark, screen, entrybox_l_at.x + 45, entrybox_l_at.y + 12)
        text(atack_c, font3, dark, screen, entrybox_c_at.x + 45, entrybox_c_at.y + 12)
        # Se dibuja text de atack rook
        text(atack_rook, font3, dark, screen, entrybox_rooks.x + 300, entrybox_rooks.y + 15)

        pygame.display.flip()

# Ventana menu
def menu():
    screen.fill(dark)  # color de la ventana

    game_button = pygame.Rect(400, 150, 200, 50)
    config_button = pygame.Rect(400, 250, 200, 50)
    salon_button = pygame.Rect(400, 350, 200, 50)
    help_button = pygame.Rect(400, 450, 200, 50)

    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_button.collidepoint(event.pos):
                    run = False
                    read_config()
                    juego()
                elif config_button.collidepoint(event.pos):
                    run = False
                    config()
                elif salon_button.collidepoint(event.pos):
                    run = False
                    high_score()
                elif help_button.collidepoint(event.pos):
                    # hacer ayuda
                    pass

        pygame.draw.rect(screen, darkpurple, game_button)
        pygame.draw.rect(screen, darkpurple, config_button)
        pygame.draw.rect(screen, darkpurple, salon_button)
        pygame.draw.rect(screen, darkpurple, help_button)

        text('Jugar', font2, green, screen, game_button.x + 100, game_button.y + 25)
        text('Configuración', font2, green, screen, config_button.x + 100, config_button.y + 25)
        text('Salon de la fama', font2, green, screen, salon_button.x + 100, salon_button.y + 25)
        text('Ayuda', font2, green, screen, help_button.x + 100, help_button.y + 25)

        pygame.display.flip()

# Ventana de login

def name():
    global user_name
    entrybox = pygame.Rect(400,300,200,50)
    button = pygame.Rect(440, 400, 140, 50)
    user_name = ""
    active = False
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if entrybox.collidepoint(event.pos):
                    active = True
                elif button.collidepoint(event.pos) and user_name != "":
                    validation(user_name)
                    run = False
                    menu()
                else:
                    active = False
            elif event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_name = user_name [0:-1]
                    elif event.key == pygame.K_TAB:
                        user_name = user_name
                    else:
                        user_name += event.unicode
        screen.fill(dark)  # color la ventana
        pygame.draw.rect(screen, brown,entrybox)
        pygame.draw.rect(screen, green, button)
        text("Ingrese su nombre", font, darkpurple, screen, 505, 105)
        text("Ingrese su nombre", font, green, screen, 500, 100)
        text(user_name, font2, white,screen, entrybox.x + 100, entrybox.y + 25)
        text("Guardar", font2, dark, screen, button.x + 70, button.y + 25)

        pygame.display.flip()

# Ventana de inicio

def start ():
    screen.fill(dark) # color de la ventana
    text("Avatar vs Rooks", font, darkpurple, screen, 505, 105)
    text("Avatar vs Rooks", font, green, screen, 500, 100)
    text("Presione una tecla para iniciar", font2, brown, screen, 500, 300)
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_5:
                    run = False
                    juego()
                elif event.key == pygame.K_9:
                    run = False
                    config()
                elif event.key == pygame.K_6:
                    run = False
                    menu()
                elif event.key == pygame.K_7:
                    run = False
                    game_over_ani()
                elif event.key == pygame.K_8:
                    run = False
                    win_ani()
                else:
                    run = False
                    name()

#Ventana de high score
def high_score():

    #Importar imagenes
    imagen_bg = pygame.image.load('resource/hg_bg.png').convert()
    imagen_bg.set_colorkey(white)
    imagen_py =  pygame.image.load('resource/playet_word.png').convert()
    imagen_py.set_colorkey(black)
    imagen_py = pygame.transform.scale(imagen_py,[100,40])
    imagen_time = pygame.image.load('resource/time_word.png').convert()
    imagen_time.set_colorkey(black)
    imagen_time = pygame.transform.scale(imagen_time, [100, 40])
    imagen_pos = pygame.image.load('resource/posicion_word.png').convert()
    imagen_pos.set_colorkey(black)
    imagen_pos = pygame.transform.scale(imagen_pos, [100, 40])



    #Crea el texto a mostar en pantalla
    create_texto_hg_list()

    #Ahorita revisar
    return_menu = pygame.Rect(380, 650, 220, 50)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 5:
                    texto_move_hg_list('down')
                elif event.button == 4:
                    texto_move_hg_list('up')
            elif  event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_DOWN :
                    pass
                elif event.key == pygame.K_UP :
                    pass
            #elif boton press
            #borrar_lista()
            #run = False
            #menu()

        # Color
        screen.fill(blue_neo)


        #Dibuja en pantalla todos los high score posibles
        draw_texts_hg_list()

        #Fondo
        screen.blit(imagen_bg,(0,0))

        #Textos
        screen.blit(imagen_py, (190, 184))
        screen.blit(imagen_time, (480, 184))
        screen.blit(imagen_pos, (680, 184))

        #Texto
        text("Salon de la Fama", font, green, screen, 500, 100)

        pygame.display.flip()

# ***************************************  Ventana juego  ************************************************

def juego():
    # Variables globales para el juego
    global MATRIZ, matrizcoin, save, time_to_start, time_last_time_new_enemy, num_rook, levels, one_time_upload_levels, list_ramdom_secs, avatar_list, coins, coin_list,total_time_in_game,time_last_time_new_coin

    # Matriz de posiciones de juego
    MATRIZ = [      [['Vacio', [250,   0]],    ['Vacio', [350,   0]],    ['Vacio', [450,   0]],    ['Vacio', [550,   0]],    ['Vacio', [650,   0]]],
                    [['Vacio', [250,  90]],    ['Vacio', [350,  90]],    ['Vacio', [450,  90]],    ['Vacio', [550,  90]],    ['Vacio', [650,  90]]],
                    [['Vacio', [250, 180]],    ['Vacio', [350, 180]],    ['Vacio', [450, 180]],    ['Vacio', [550, 180]],    ['Vacio', [650, 180]]],
                    [['Vacio', [250, 270]],    ['Vacio', [350, 270]],    ['Vacio', [450, 270]],    ['Vacio', [550, 270]],    ['Vacio', [650, 270]]],
                    [['Vacio', [250, 360]],    ['Vacio', [350, 360]],    ['Vacio', [450, 360]],    ['Vacio', [550, 360]],    ['Vacio', [650, 360]]],
                    [['Vacio', [250, 450]],    ['Vacio', [350, 450]],    ['Vacio', [450, 450]],    ['Vacio', [550, 450]],    ['Vacio', [650, 450]]],
                    [['Vacio', [250, 540]],    ['Vacio', [350, 540]],    ['Vacio', [450, 540]],    ['Vacio', [550, 540]],    ['Vacio', [650, 540]]],
                    [['Vacio', [250, 630]],    ['Vacio', [350, 630]],    ['Vacio', [450, 630]],    ['Vacio', [550, 630]],    ['Vacio', [650, 630]]],
                    [['Vacio', [250, 720]],    ['Vacio', [350, 720]],    ['Vacio', [450, 720]],    ['Vacio', [550, 720]],    ['Vacio', [650, 720]]]         ]

    # Matriz de monedas
    matrizcoin = [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None],
                  [None], [None], [None]]

    # Variables con la funcionalidad de los niveles

    levels = [True, True, True]

    one_time_upload_levels = [True, True, True]

    # Rango de secs aleatorio
    list_ramdom_secs = 0

    # Numero de Moendas en el juego
    coins = 100

    # Lista de avarts que faltan de poner
    avatar_list = []

    # Numero de identificador del Rook
    num_rook = 1001

    # Variables relacionadas con el tiempo
    total_time_in_game = 0

    time_to_start = pygame.time.get_ticks() / 1000

    time_last_time_new_enemy = time_to_start

    time_last_time_new_coin = time_to_start

    global quit_rook_var, game_over, shop_open

    shop_open = True
    game_over = False
    quit_rook_var = False

    # Importa imagenes del escenario
    matriz_0_dibujo = pygame.image.load('resource/matriz_0.png').convert()
    matriz_1_dibujo = pygame.image.load('resource/matriz_1.png').convert()
    matriz_2_dibujo = pygame.image.load('resource/matriz_2.png').convert()
    matriz_3_dibujo = pygame.image.load('resource/matriz_3.png').convert()

    #Boton de guardado
    image_save = pygame.image.load('resource/save.jpg').convert()
    image_save = pygame.transform.scale(image_save, [200, 100])
    image_save.set_colorkey(white)
    save_button = pygame.Rect(787, 260, 173 , 80)


    # botones tienda
    sand_button = pygame.Rect(0, 500, 100, 80)
    rock_button = pygame.Rect(0, 580, 100, 80)
    fire_button = pygame.Rect(0, 660, 100, 80)
    water_button = pygame.Rect(0, 740, 100, 80)
    quit_button = pygame.Rect(900, 500, 100, 80)

    # Cosas que necesita rooks
    tipo = 0

    # Revisa si hay una partida por cargar
    login()

    while not game_over:
        #Tiempo de ahorita del juego
        secs_now = int(total_time_in_game-time_to_start+pygame.time.get_ticks()/1000)
        # Fin del juego
        you_lost_game()
        # Eventos
        for event in pygame.event.get():
            # Salida abruta del juego
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                exit()
            # Eventos del mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Valida si presiono el boton de quitar el rook
                if quit_button.collidepoint(event.pos):
                    quit_rook_var = True
                elif quit_rook_var:
                    mouse_pos = pygame.mouse.get_pos()
                    click_posicion(mouse_pos)
                # Valida si presiono el boton de tienda
                elif shop_open:
                    if coins > 0:
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
                    rook_posicion(tipo, pygame.mouse.get_pos())

                # Si presiona el boton de guardar
                if save_button.collidepoint(event.pos):
                    save()

        # Primer Nivel
        if levels[0]:

            screen.fill(white)

            # Dibujos de botones
            pygame.draw.rect(screen, brown, sand_button)
            pygame.draw.rect(screen, lightgreen, rock_button)
            pygame.draw.rect(screen, green, fire_button)
            pygame.draw.rect(screen, purple, water_button)
            pygame.draw.rect(screen, darkpurple, quit_button)

            # VERIFICAR SI AQUI VA UN DRAW PARA SAVE
            pygame.draw.rect(screen, green, save_button)
            screen.blit(image_save, [775, 250])

            #Monedas
            text(str(coins), font2, brown, screen, 100, 50)

            #Nivel
            text('Nivel 1', font2, brown, screen, 100, 200)

            #Tiempo
            text('Tiempo: '+str( secs_now)+'s', font2, brown, screen, 852, 400)

            
            # Pone la cantidad de enemigo y monedas en este nivel
            start_config_level_1()

            # Revisa las colisiones
            atacks_colsion_check_avart()
            atacks_colsion_check_rook()

            screen.blit(matriz_1_dibujo, [250, 0])
            draw_objetcs_matriz()

            # Parte funcional para que disparen los rooks
            atacks_rooks()
            list_atacks_rooks.draw(screen)
            # atacks_move()--------------------------------------------------------------------------

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
                levels[0] = False
                limpiar_matriz()

        # Segundo Nivel
        elif levels[1]:

            screen.fill(purple)

            # Dibujos de botones y texto
            pygame.draw.rect(screen, brown, sand_button)
            pygame.draw.rect(screen, lightgreen, rock_button)
            pygame.draw.rect(screen, green, fire_button)
            pygame.draw.rect(screen, purple, water_button)
            pygame.draw.rect(screen, darkpurple, quit_button)

            #  AQUI VA UN DRAW PARA SAVE
            pygame.draw.rect(screen, white, save_button)
            screen.blit(image_save, [775, 250])

            #Monedas
            text(str(coins), font2, brown, screen, 100, 50)

            #Nivel
            text('Nivel 2', font2, brown, screen, 100, 200)

            #Tiempo
            text('Tiempo: '+str(secs_now)+'s', font2, brown, screen,852, 400)

            # Pone la cantidad de enemigo en este nivel
            start_config_level_2()

            # Revisa las colisiones
            atacks_colsion_check_avart()
            atacks_colsion_check_rook()

            screen.blit(matriz_2_dibujo, [250, 0])
            draw_objetcs_matriz()

            # Parte funcional para que disparen los rooks
            atacks_rooks()
            list_atacks_rooks.draw(screen)
            # atacks_move()---------------------------------------------------------------------------

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
                levels[1] = False
                limpiar_matriz()

        # Tercer Nivel
        elif levels[2]:

            screen.fill(darkpurple)

            # Dibujos de botones y texto
            pygame.draw.rect(screen, brown, sand_button)
            pygame.draw.rect(screen, lightgreen, rock_button)
            pygame.draw.rect(screen, green, fire_button)
            pygame.draw.rect(screen, purple, water_button)
            pygame.draw.rect(screen, darkpurple, quit_button)

            #  AQUI VA UN DRAW PARA SAVE
            pygame.draw.rect(screen, white, save_button)
            screen.blit(image_save, [775, 250])

            #Monedas
            text(str(coins), font2, brown, screen, 100, 50)

            #NIVEL
            text('Nivel 3', font2, brown, screen, 100, 200)

            #Tiempo
            text('Tiempo: '+str(secs_now)+'s', font2, brown, screen, 852, 400)



            # Pone la cantidad de enemigo en este nivel
            start_config_level_3()

            # Revisa las colisiones
            atacks_colsion_check_avart()
            atacks_colsion_check_rook()

            screen.blit(matriz_3_dibujo, [250, 0])
            draw_objetcs_matriz()

            # Parte funcional para que disparen los rooks
            atacks_rooks()
            list_atacks_rooks.draw(screen)
            # atacks_move()-----------------------------------------------------------------

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

        #Gano el juego
        else:
            game_over = True
            limpiar_matriz()
            high_score_save()
            win_ani()

        clock.tick(60)
        pygame.display.flip()

# Iniciar el juevo

start()

