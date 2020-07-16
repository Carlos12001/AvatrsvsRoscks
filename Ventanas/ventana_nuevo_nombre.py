import pygame, sys
from GameV0 import *

global MATRIZ, coins2, MATRIZ_NEW, coins_new, player_name

# matriz a cargar limpia
MATRIZ_NEW = [  [['Vacio', [250,   0]],    ['Vacio', [350,   0]],   ['Vacio', [450,    0]],    ['Vacio', [550,   0]],    ['Vacio', [650,   0]]],
                [['Vacio', [250,  90]],    ['Vacio', [350,  90]],   ['Vacio', [450,   90]],    ['Vacio', [550,  90]],    ['Vacio', [650,  90]]],
                [['Vacio', [250, 180]],    ['Vacio', [350, 180]],   ['Vacio', [450,  180]],    ['Vacio', [550, 180]],    ['Vacio', [650, 180]]],
                [['Vacio', [250, 270]],    ['Vacio', [350, 270]],   ['Vacio', [450,  270]],    ['Vacio', [550, 270]],    ['Vacio', [650, 270]]],
                [['Vacio', [250, 360]],    ['Vacio', [350, 360]],   ['Vacio', [450,  360]],    ['Vacio', [550, 360]],    ['Vacio', [650, 360]]],
                [['Vacio', [250, 450]],    ['Vacio', [350, 450]],   ['Vacio', [450,  450]],    ['Vacio', [550, 450]],    ['Vacio', [650, 450]]],
                [['Vacio', [250, 540]],    ['Vacio', [350, 540]],   ['Vacio', [450,  540]],    ['Vacio', [550, 540]],    ['Vacio', [650, 540]]],
                [['Vacio', [250, 630]],    ['Vacio', [350, 630]],   ['Vacio', [450,  630]],    ['Vacio', [550, 630]],    ['Vacio', [650, 630]]],
                [['Vacio', [250, 720]],    ['Vacio', [350, 720]],   ['Vacio', [450,  720]],    ['Vacio', [550, 720]],    ['Vacio', [650, 720]]]  ]

# monedas limpias
coins_new = 0

player_name = ""
# --------------------------------------------- Clases ---------------------------------------#

# --------------------------------------------- Funciones ---------------------------------------------- #
# -------------------------------------- Funcion para crear texto -------------------------------------- #

def text(text, font, color, surface, x, y):
    txtobj = font.render(text, 1, color)
    txtrect = txtobj.get_rect()
    txtrect.center = (x, y)
    surface.blit(txtobj, txtrect)

# Funciones para el cargado de partidas guardadas o nuevas
# validacion si el usuario guardo
def validation (name):
    global MATRIZ, MATRIZ_NEW, coins_new
    name = str(name)
    ruta = "game_save.txt"
    file = open(ruta, "r")
    for line in file:
        line = line.rstrip('\n')
        if line == name:
            print("juego cargado")
            load_game()
            break
        else:
            MATRIZ = MATRIZ_NEW
            coins2 = coins_new
            #save_name(name)
            print("no se cargo")
            #print(MATRIZ)
            #print(coins2)
    file.close()

def save_name(name):
    global player_name
    player_name = name
    print("guarde nombre")
    ruta = "player_name.txt"
    file = open(ruta, "w")
    file.write(name)
    file.write('\n')
    file.write("Tiempo" + '\n')
    file.write("000")
    file.write('\n')
    file.close()

def load_game():
    global MATRIZ
    MATRIZ = []
    global coins2
    coins2 = 0
    ruta = "game_save.txt"
    file = open(ruta, "r")
    cont = 0
    for line in file:
        line.splitlines()
        line = line.rstrip('\n')
        if cont == 0:
            player_name = line
            cont += 1
        elif cont == 2:
            MATRIZ = line
            cont += 1
        elif cont == 4:
            coins2 += int(line)
        else:
            cont += 1
    print(player_name)
    print(list(MATRIZ))
    print(type(MATRIZ))
    print(coins2)
    print("listo")
    file.close()




# ---------------------- Ventana dodne el jugador digita su nombre por primera vez --------------------- #

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
                    validation (user_name)
                    run = False
                    from Ventanas import ventana_de_menu
                else:
                    active = False

            elif event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_name = user_name [0:-1]
                    elif event.key == pygame.K_TAB:
                        user_name = user_name
                    #elif event.key == pygame.K_
                    else:
                        user_name += event.unicode

                #from Ventanas import ventana_de_menu
                #run = False
        screen.fill(dark)  # color la ventana
        pygame.draw.rect(screen, brown,entrybox)
        pygame.draw.rect(screen, green, button)
        text("Ingrese su nombre", font, darkpurple, screen, 505, 105)
        text("Ingrese su nombre", font, green, screen, 500, 100)
        text(user_name, font2, white,screen, entrybox.x + 100, entrybox.y + 25)
        text("Guardar", font2, dark, screen, button.x + 70, button.y + 25)


        pygame.display.flip()




        # entrada texto del nombre
        # escribir el nombre del jugador en un txt


name()
