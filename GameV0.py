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
black = (0, 0, 0)

pygame.init()
pygame.font.init()
pygame.display.set_caption("Avatar vs Rooks")

screen = pygame.display.set_mode(size)

font = pygame.font.SysFont("Times New Roman", 50)
font2 = pygame.font.SysFont("Times New Roman", 30)
font3 = pygame.font.SysFont("Times New Roman", 20)

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
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_5:
                    run = False
                    from Ventanas import ventana_de_juego
                #elif event.key == pygame.K_9:
                 #   run = False
                  #  from Ventanas import ventana_config
                #elif event.key == pygame.K_6:
                 #   run = False
                  #  from Ventanas import  ventana_de_menu
                else:
                    run = False
                    from Ventanas import ventana_nuevo_nombre



start()





























