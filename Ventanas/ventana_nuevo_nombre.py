import pygame, sys
from GameV0 import *

# --------------------------------------------- Clases ---------------------------------------#

#color_inactive = brown
#color_active = white

#class Entry():
 #   def __init__(self, x, y, width, height, text = ""):
  #      self.rect = pygame.Rect(x,y,width, height)
   #     self.color = color_inactive
    #    self.text = text
     #   self.txtsurface = font2.render(text,True,self.color)
      #  self.active = False

    #def type_entry (self, event):
     #   if event.type == pygame.MOUSEBUTTONDOWN:
      #      if self.rect.collidepoint(event.pos): # Cuando el usuario presione el cuadro
       #         self.active = not self.active # Se activa el color
        #    else:
         #       self.active = False
          #  self.color = color_active # cambia el color de la caja de txt
        #elif event.type == pygame.K_RETURN:
         #   if self.active:
          #      if event.key == pygame.K_RETURN:
           #         print(self.text)
            #        self.text = ""
             #   elif event.key == pygame.K_BACKSPACE:
              #      self.text = self.text[:-1]
               # else:
                #    self.text += event.unicode
                #self.txt_surface = font2.render(self.text, True, self.color)

    #def update(self): # Acomoda el cuadro en caso de ser un texto muy largo
     #   width = max(200, self.txt_surface.get_width() + 10)
      #  self.rect.w = width

    #def draw(self, screen):
     #   screen.blit(self.txtsurface, (self.rect.x + 5, self.rect.y + 5))
      #  pygame.draw.rect(screen, self.color, self.rect, 2)

class Entry:
    def __init__(self,x,y):
        self.line = 0 # Mostrar en cada linea una letra
        self.letters = ["",] # Mostrar caracteres
        self.font = pygame.font.Font(None, 25)
        self.distance = 20
        self.posX = x
        self.posY = y
    def keys(self, event):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_RETURN:
                    self.letters.append("")
                    self.line += 1
                elif event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.K_BACKSPACE:
                    if self.letters[self.line] == "" and self.line > 0:
                        self.letters = self.letters[0: -1]
                        self.line -= 1
                    else:
                        self.letters[self.line] += self.letters[self.line][0:-1]
                else:
                    self.letters[self.line] = strg(self.letters[self.line] + event.unicode)
    def mensaje (self, surface):
        screen.fill(brown)
        for self.line in range(len(self.letters)):
            letter_render = self.font.render(self.letters[self.line], True, white)
        screen.blit(letter_render, (self.posX, self.posY + self.distance * self.line))
# --------------------------------------------- Funciones ---------------------------------------------- #
# -------------------------------------- Funcion para crear texto -------------------------------------- #

def text(text, font, color, surface, x, y):
    txtobj = font.render(text, 1, color)
    txtrect = txtobj.get_rect()
    txtrect.center = (x, y)
    surface.blit(txtobj, txtrect)


# ---------------------- Ventana dodne el jugador digita su nombre por primera vez --------------------- #


def name():
    entrybox = pygame.Rect(400,300,200,50)
    user_name = ""
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_name = user_name [0:-1]
                else:
                    user_name += event.unicode
                #from Ventanas import ventana_de_menu
                #run = False

        screen.fill(dark)  # color la ventana
        pygame.draw.rect(screen, brown,entrybox)
        text("Ingrese su nombre", font, darkpurple, screen, 505, 105)
        text("Ingrese su nombre", font, green, screen, 500, 100)
        text(user_name, font2, white,screen, entrybox.x + 100, entrybox.y + 25)

        
        pygame.display.flip()




        # entrada texto del nombre
        # escribir el nombre del jugador en un txt


name()
