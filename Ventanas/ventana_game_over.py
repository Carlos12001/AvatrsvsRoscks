import pygame, sys

from GameV0 import *

class animacion (pygame.sprite.Sprite):
    def __init__(self, image, position, width, height,frames_t):
        super().__init__()
        self.sheet = pygame.image.load(image) # cambiar nombre
        self.sheet.set_clip(pygame.Rect(0, 0, width, height))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.frame = 0
        self.states = []
        for frame in range(frames_t):
            self.states.append([width * frame, 0, width, height])

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))


    def update(self):
        self.clip(self.states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())


def game_over_ani():

    sprite = animacion('resource/gameover.png', (480,450), 99, 96, 14)

    again = pygame.Rect(390, 650, 220, 50)
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if again.collidepoint(event.pos):
                    sprite.kill()
                    import GameV0
                    start()

        sprite.update()
        screen.fill(dark)  # color la ventana
        screen.blit(sprite.image, sprite.rect)

        pygame.draw.rect(screen, brown, again)
        text("Game Over", font4, darkpurple, screen, 505, 305)


        pygame.display.flip()
        clock.tick(10)

game_over_ani()