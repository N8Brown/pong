import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 370
        self.rect.y = 245
        self.speed = 10
        self.dx = 1
        self.dy = 1
