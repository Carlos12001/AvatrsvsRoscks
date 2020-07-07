import pygame, sys

size = (1000, 800)

# Colores

dark = (34,32,53)
darkpurple = (87,82,103)
purple = (210, 149, 222)
lightgreen = (160,255,227)
green = (101,220,152)
brown = (141,137,128)
white = (255, 255, 255)

pygame.init()
pygame.font.init()
pygame.display.set_caption("Avatar vs Rooks")

screen = pygame.display.set_mode(size)

font = pygame.font.SysFont("Times New Roman", 50)
font2 = pygame.font.SysFont("Times New Roman", 30)

# --------------------------------------------- Funciones ---------------------------------------------- #
# -------------------------------------- Funcion para crear texto -------------------------------------- #
        
def text (text, font, color, surface, x , y):
    txtobj = font.render(text, 1, color)
    txtrect = txtobj.get_rect()
    txtrect.center = (x, y)
    surface.blit (txtobj, txtrect)


# ------------------------------ Es la ventana de inicio del juego Titulo ------------------------------- #

def start ():
    screen.fill (dark) # color de la ventana
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
            if event.type == pygame.KEYUP:
                run = False

# ---------------------- Ventana dodne el jugador digita su nombre por primera vez --------------------- #

def name ():
    screen.fill (dark) # color la ventana
    text("Ingrese su nombre", font, darkpurple, screen, 505, 105)
    text("Ingrese su nombre", font, green, screen, 500, 100)
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                run = False
        # entrada texto del nombre 
        # escribir el nombre del jugador en un txt
        
# ------------------------------- Pantalla de inicio del menu del juego ------------------------------- #

def menu():
    screen.fill(green) # color de la ventana
    text('Jugar', font2, screen, 500,150)
    text('Configuración', font2, screen, 500,150)
    text('Salon de la fama', font2, screen, 500,150)
    text('Ayuda', font2, screen, 500,150)

    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
                
# ------------------------------- Pantalla de inicio del menu del juego ------------------------------- #
def juego():
    screen.fill(white)
    #Imagen de fondos
    #Por ahorita es el fondo blanco
    #background = pygame.image.load('fonfo.png').convert()
    #screen.fill(background,[0,0])

    pygame.draw.rect(screen, purple, (125, 0, 750, 800))
    

# ----------------------------------------------- CLASES ----------------------------------------------- #
# --------------------------------------- Clase entrada de texto --------------------------------------- #

class Entry:
    def __init__(self,x,y):
        self.line = 0 # Mostrar en cada linea una letra
        self.letters = ["",] # Mostrar caracteres
        self.font = pygame.font.Font("Times New Roman", 25)
        self.distance = 20
        self.posX = x
        self.posY = y
    def keys(self, event):
        for event in events:
            if action.type == KEYDOWN:
                if action.key == RETURN:
                    self.letters.append("")
                    self.line += 1
                elif action.key == K_SCAPE:
                    pygame.quit()
                    sys.exit()
                elif action.key == K_BACKSPACE:
                    if self.letters[self.lineas] == "" and self.lineas > 0:
                        self.letters =
    def mensaje (self, surface):
        pass





# ----------------------------------- Controlador del juego ------------------------------------------- #

  
start()
name()

