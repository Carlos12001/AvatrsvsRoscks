import pygame,sys,random
from GameV0 import *
from Objetos import AvartsV0
from Objetos import RooksV0
from Objetos import CoinsV0

#Variables Globales a Necesitar


#Matriz de posiciones de juego
global MATRIZ, all_sprites_matriz_list, time_to_start, time_last_time_new_enemy, matrizcoin
MATRIZ = [    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [0, 0]],    ['Vacio', [0, 0]],   ['Vacio', [0, 0]],    ['Vacio', [0, 0]],    ['Vacio', [0, 0]],
              ['Vacio', [250, 0]],    ['Vacio', [350, 0]],   ['Vacio', [450, 0]],    ['Vacio', [550, 0]],    ['Vacio', [650, 0]]   ]

matrizcoin = [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None]]
all_sprites_matriz_list =  pygame.sprite.Group ()

time_to_start = pygame.time.get_ticks()/1000

time_last_time_new_enemy = time_to_start

time_last_time_new_coin = time_to_start

# funcion texto
def text(text, font, color, surface, x, y):
    txtobj = font.render(text, 1, color)
    txtrect = txtobj.get_rect()
    txtrect.center = (x, y)
    surface.blit(txtobj, txtrect)




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
    global rook_list
    rook_list = []
    rook_list_in_game = pygame.sprite.Group()

    # Conjunto de monedas
    global coin_list
    #coin_list = pygame.sprite.Group()
    coin_list = []
    for i in range(20):
        coin = CoinsV0.New_Coin(random.randint(1,4))
        #coin_list.add(coin)
        coin_list.append(coin)


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

    # Creacion de Rooks segun donde es presionado

    def new_rook( tipo):
        if tipo == 5:
            rook = RooksV0.Rooks(tipo)
            rook_list.append(rook)
            print(rook_list)
        elif tipo == 6:
            rook = RooksV0.Rooks(tipo)
            rook_list.append(rook)
            print(rook_list)
        elif tipo == 7:
            rook = RooksV0.Rooks(tipo)
            rook_list.append(rook)
            print(rook_list)
        elif tipo == 8:
            rook = RooksV0.Rooks(tipo)
            rook_list.append(rook)
            print(rook_list)


    coins = 500
    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if coins > 0:
                    if coins >= 50 and sand_button.collidepoint(event.pos):
                        coins -= 50
                        tipo = 5  # revisar coordenadas
                        print("sand")
                        new_rook(tipo)
                    elif coins >= 100 and rock_button.collidepoint(event.pos):
                        coins -= 100
                        tipo = 6  # revisar coordenadas
                        print("rock")
                        new_rook(tipo)
                    elif coins >= 150 and fire_button.collidepoint(event.pos):
                        coins -= 150
                        tipo = 7  # revisar coordenadas
                        print("fire")
                        new_rook(tipo)
                    elif coins >= 150 and water_button.collidepoint(event.pos):
                        coins -= 150
                        tipo = 8  # revisar coordenadas
                        print("water")
                        new_rook(tipo)
                    else:
                        coins = coins
                else:
                    coins = 0


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

            put_new_coin()
            draw_coins()

        clock.tick(60)
        pygame.display.flip()

def put_new_enemy(list_ramdom_secs):
    global time_last_time_new_enemy
    time = random.randint(1,15)
    if time == int(pygame.time.get_ticks()//1000 - time_last_time_new_enemy) :
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
                done = True
                break
            else:
                #print('Estoy lleno')
                pass

        if done:
            break

def put_new_rook_aux():
    global rook_list
    if rook_list != []:
        for rook in rook_list:
            for i in MATRIZ:
                for estado in MATRIZ[i]:
                    # colocar metodo de posicion y se verifica
                    if estado[0] == "Vacio" and rook.posicion_get() == estado[1][0]: # crear metodo posicionget()
                        estado[0] = rook
                        rook_list = rook_list[1:]
    else:
        print("no compro rook, compre!!")


def draw_objetcs_matriz():
    global all_sprites_matriz_list,MATRIZ
    for cuadrito in MATRIZ:
        object = cuadrito[0]
        if object != 'Vacio':
            object.draw_me()


def put_new_coin():
    global time_last_time_new_coin
    global coin_list
    time = random.randint(1,10)
    if time == int(pygame.time.get_ticks()//1000 - time_last_time_new_coin) :
        time_last_time_new_coin = pygame.time.get_ticks()//1000
        return put_new_coin_aux()

def put_new_coin_aux():
    global  matrizcoin
    global coin_list
    done = False
    #print('Me llamaron')
    for coin in coin_list:
        for coin2 in matrizcoin:
            #print("1234")
            if coin2[0] == None:
                coin2[0] = coin
                coin_list = coin_list[1:]
                print('moneda puesto', 'Quedan en total sin poner', len(coin_list))
                done = True
                break
            else:
                #print('Estoy lleno')
                pass

        if done:
            print('termine de poner moneda')
            break

def draw_coins ():
    global matrizcoin
    #print(matrizcoin)
    for moneda in matrizcoin:
        coins = moneda[0]
        if coins != None:
            #print(coins.type_get(),coins.posicion_get())
            coins.draw_me()

#def draw_coins (coin_list):
 #   for coin in coin_list:
  #      coin.draw_me()







juego()