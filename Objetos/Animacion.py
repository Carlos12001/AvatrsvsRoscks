import pygame

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

    def update(self, screen):
        self.clip(self.states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        screen.blit(self.image, self.rect)