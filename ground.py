import pygame
from pygame import Vector2

class Ground(object):
    def __init__(self,screen):
        self.screen = screen
        self.size = (1300,50)

        self.image = pygame.image.load("upload\\ground.png")

        self.rect = self.image.get_rect()
        self.pos = Vector2(0, self.screen.get_height()-100)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def draw(self):
        pygame.transform.scale(self.image, (1300,50))
        self.screen.blit(self.image, [self.pos.x, self.pos.y])
