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

clock = pygame.time.Clock()
# --------------------------------------------- Funciones ---------------------------------------------- #
# -------------------------------------- Funcion para crear texto -------------------------------------- #
        
def text (text, font, color, surface, x , y,backgrounf=None):
    txtobj = font.render(text, 1, color,backgrounf)
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
                from Ventanas import ventana_nuevo_nombre







# ----------------------------------------------- CLASES ----------------------------------------------- #
# --------------------------------------- Clase entrada de texto --------------------------------------- #


#Esto deberia ir en objetos
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
                    if self.letters[self.line] == "" and self.line > 0:
                        self.letters = self.letters[0: -1]
                        self.line -= 1
                    else:
                        self.letters[self.line] = self.letters[self.line][0:-1]
                else:
                    self.letters[self.line] = srt(self.letters[self.line] + accion.unicode)
    def mensaje (self, surface):
        screen.fill(brown)
        for self.line in len(self.letters):
            letter_render = self.font.render(self.letters[self.line], True, dark)
            screen.blit(letter_render, self.posX, self.posY + self.distance * self.line)



























# ----------------------------------- Controlador del juego ------------------------------------------- #
start()





























