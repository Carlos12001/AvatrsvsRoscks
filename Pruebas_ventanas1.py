import pygame, sys

size = (1000, 500)

# Colores

dark = (34,32,53)
darkpurple = (87,82,103)
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

#class text:
#    def __init__ (self, txt, font, color, surface, x, y):
 #       self.txtobj = font.render(text, 1, color)
  #      self.rect = txtobj.get_rect()
   #     self.rect.center = (x, y)
    #    self.surface.blit (txtobj, txtrect)

    #def rendertxt (self, txt, font, color, surface, x, y):

 
 # -------------------------------------- Funcion para crear texto -------------------------------------- #
        
def text (text, font, color, surface, x , y):
    txtobj = font.render(text, True, color)
    txtrect = txtobj.get_rect()
    txtrect.center = (x, y)
    surface.blit (txtobj, txtrect)

#Es la ventana de inicio del juego Titulo
def start ():
    screen.fill (dark)
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
# ---------------------------- Ventana dodne el jugador digita su nombre por primera vez --------------------#

def name ():
    screen.fill (dark)
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


                
start()
name()

