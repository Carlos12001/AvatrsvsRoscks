import pygame,sys,random
from GameV0 import *
from Objetos import AvartsV0
from Objetos import RooksV0
from Objetos import CoinsV0

#Variables Globales a Necesitar


#Matriz de posiciones de juego
#Variables a utilizar en
global MATRIZ, all_sprites_matriz_list, time_to_start, time_last_time_new_enemy
MATRIZ = [    [['Vacio', [250, 0]],    ['Vacio', [350, 0]],   ['Vacio', [450, 0]],    ['Vacio', [550, 0]],    ['Vacio', [650, 0]]],
              [['Vacio', [250, 0]],    ['Vacio', [350, 0]],   ['Vacio', [450, 0]],    ['Vacio', [550, 0]],    ['Vacio', [650, 0]]],
              [['Vacio', [250, 0]],    ['Vacio', [350, 0]],   ['Vacio', [450, 0]],    ['Vacio', [550, 0]],    ['Vacio', [650, 0]]],
              [['Vacio', [250, 0]],    ['Vacio', [350, 0]],   ['Vacio', [450, 0]],    ['Vacio', [550, 0]],    ['Vacio', [650, 0]]],
              [['Vacio', [250, 0]],    ['Vacio', [350, 0]],   ['Vacio', [450, 0]],    ['Vacio', [550, 0]],    ['Vacio', [650, 0]]],
              [['Vacio', [250, 0]],    ['Vacio', [350, 0]],   ['Vacio', [450, 0]],    ['Vacio', [550, 0]],    ['Vacio', [650, 0]]],
              [['Vacio', [250, 0]],    ['Vacio', [350, 0]],   ['Vacio', [450, 0]],    ['Vacio', [550, 0]],    ['Vacio', [650, 0]]],
              [['Vacio', [250, 0]],    ['Vacio', [350, 0]],   ['Vacio', [450, 0]],    ['Vacio', [550, 0]],    ['Vacio', [650, 0]]],
              [['Vacio', [250, 0]],    ['Vacio', [350, 0]],   ['Vacio', [450, 0]],    ['Vacio', [550, 0]],    ['Vacio', [650, 0]]]   ]

matrizcoin = [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None]]
all_sprites_matriz_list =  pygame.sprite.Group ()

time_to_start = pygame.time.get_ticks()/1000

time_last_time_new_enemy = time_to_start

time_last_time_new_coin = time_to_start

# funcion texto
#def text(text, font, color, surface, x, y):
 #   txtobj = font.render(text, 1, color)
  #  txtrect = txtobj.get_rect()
   # txtrect.center = (x, y)
    #surface.blit(txtobj, txtrect)

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
    if 15 == int(pygame.time.get_ticks()//1000 - time_last_time_new_enemy) :
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
                print('enemigo puesto','Quedan en total sin poner',len(avatar_list))
                done = True
                break
            else:
                #print('Estoy lleno')
                pass

        if done:

            break
#Dibuja el los objetos de la matriz
def draw_objetcs_matriz():
    global all_sprites_matriz_list,MATRIZ
    for fila in MATRIZ:
        for cuadrito in fila:    
            object = cuadrito[0]
            if object != 'Vacio':
                object.draw_me(pygame.time.get_ticks())

def move_enemy():
    global MATRIZ,game_over
    i_now = -1

    for fila in MATRIZ:
        i_now+=1
        j = -1
        for cuadrito in fila:
            j+=1
            #Revisa si hay personaje
            if cuadrito [0] != 'Vacio':

                #Revisa si es un enemigo
                if cuadrito[0].type_get() == 'Arquero' or cuadrito[0].type_get() == 'Escudero'\
                or cuadrito[0].type_get() == 'Lenador' or cuadrito[0].type_get() == 'Canival':

                    #Revisa si es posible el cambio
                    if MATRIZ[i_now-1][j][0] == 'Vacio':

                        if cuadrito[0].update(pygame.time.get_ticks(),'move'):
                            MATRIZ[i_now-1][j][0] = cuadrito[0]
                            cuadrito[0] = 'Vacio'

# Funciones para el funcionamiento de las monedas
def put_new_coin():
    global time_last_time_new_coin
    global coin_list
    time = random.randint(5,10)
    if time == int(pygame.time.get_ticks()//1000 - time_last_time_new_coin) :
        time_last_time_new_coin = pygame.time.get_ticks()//1000
        return put_new_coin_aux()

def put_new_coin_aux():
    global  matrizcoin
    global coin_list
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

# Creacion de Rooks segun donde es presionado

def new_rook(tipo):
    pos = RooksV0.position(True) 
    if tipo == 5:
        rook += [RooksV0.New_Rook(tipo), pos]
        print(rook)
        #rook_list.append(rook)

    elif tipo == 6:
        rook += [RooksV0.New_Rook(tipo), pos]
        #rook_list.append(rook)

    elif tipo == 7:
        rook += [RooksV0.New_Rook(tipo), pos]
        #rook_list.append(rook)

    elif tipo == 8:
        rook += [RooksV0.New_Rook(tipo), pos]
        #rook_list.append(rook)

def put_new_rook_aux():
    global rook
    for fila in MATRIZ:
        for cuadrito in fila:
            if rook == []:
                pass
            # colocar metodo de posicion y se verifica
            elif cuadrito[0] == "Vacio" and rook[1] == cuadrito[1]:
                cuadrito[0] = rook[0]
                rook = []

# ------------------------------- Pantalla de inicio del menu del juego ------------------------------- #


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

    # Conjunto rooks
    global rook
    rook = []

    # Conjunto de monedas
    global coins
    coins = 0
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
        for i in range(50):
            avatar = AvartsV0.New_Avart(range(1,4))
            avatar_list.append(avatar)

    # Creacion de Rooks segun donde es presionado

    #def new_rook(tipo):
     ##      rook = RooksV0.Rooks(tipo)
       #     rook_list.append(rook)
        #    print(rook_list)
        #elif tipo == 6:
         #   rook = RooksV0.Rooks(tipo)
          #  rook_list.append(rook)
           # print(rook_list)
        #elif tipo == 7:
         #   rook = RooksV0.Rooks(tipo)
          #  rook_list.append(rook)
           # print(rook_list)
        #elif tipo == 8:
         #   rook = RooksV0.Rooks(tipo)
          #  rook_list.append(rook)
           # print(rook_list)


    global game_over
    shop_open = True
    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
                exit()
            if shop_open == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if coins > 0:
                        if coins >= 50 and sand_button.collidepoint(event.pos):
                            coins -= 50
                            tipo = 5  # revisar coordenadas
                            shop_open = False
                            print("sand")
                            new_rook(tipo)
                        elif coins >= 100 and rock_button.collidepoint(event.pos):
                            coins -= 100
                            tipo = 6  # revisar coordenadas
                            shop_open = False
                            print("rock")
                            new_rook(tipo)
                        elif coins >= 150 and fire_button.collidepoint(event.pos):
                            coins -= 150
                            tipo = 7  # revisar coordenadas
                            shop_open = False
                            print("fire")
                            new_rook(tipo)
                        elif coins >= 150 and water_button.collidepoint(event.pos):
                            coins -= 150
                            tipo = 8  # revisar coordenadas
                            shop_open = False
                            print("water")
                            new_rook(tipo)
                        else:
                            coins = coins
                    else:
                        coins = 0

        #Pierde el juego
        for enemy_false in MATRIZ[0]:
            if enemy_false[0] !='Vacio':
                #game_over = True
                #import GameV0
                #GameV0.start()
                break

        #Primer Nivel


        screen.fill(white)

        pygame.draw.rect(screen, brown, sand_button)
        pygame.draw.rect(screen, lightgreen, rock_button)
        pygame.draw.rect(screen, green, fire_button)

        pygame.draw.rect(screen, purple, water_button)
        text(str(coins), font2,brown, screen,100,50)




        if level_1:
            screen.blit(matriz_0_dibujo, [250, 0])
            draw_objetcs_matriz()

            put_new_enemy(list_ramdom_secs)
            move_enemy()
            put_new_coin()
            draw_coins()
            kill_coins()
            put_new_rook_aux()

        clock.tick(60)
        pygame.display.flip()

juego()


def new_rook_pos(set):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    while set:
        # primer fila
        if 200 < mouse_pos[0] < 300 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 89:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 250
            rectY = 45
            set = False
            return rectX, rectY
        elif 300 < mouse_pos[0] < 400 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 89:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX= 350
            rectY = 45
            set = False
            return rectX, rectY
        elif 400 < mouse_pos[0] < 500 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 89:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX= 450
            rectY = 45
            set = False
            return rectX, rectY
        elif 500 < mouse_pos[0] < 600 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 89:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 550
            rectY = 45
            set = False
            return rectX, rectY
        elif 600 < mouse_pos[0] < 700 and mouse_click[0] == 1 and 0 < mouse_pos[1] < 89:
            # posicionar cada self.type_rook en un a posicion estandar
            rectX = 650
            rectY = 45
            set = False
            return rectX, rectY






