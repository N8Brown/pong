import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):
    def __init__(self, side):
        Sprite.__init__(self)
        self.image = pygame.Surface((10, 75))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.points = 0
        self.speed = 10
        if side == "left":
            self.rect.x = 25
            self.rect.y = 225
        elif side == "right":
            self.rect.x = 715
            self.rect.y = 225
