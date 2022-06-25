import pygame, random
from pygame.math import Vector2

class Rock(object):
    def __init__(self,game):
        self.game = game
        self.image = pygame.image.load("upload\\objects\\rock.png")
        self.rect = self.image.get_rect()
        self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 79), -random.randint(200, 400))
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.gravity = self.game.gravity
        self.speed = 0.3
        self.object_delta = 0.0
        self.speed_down = 60.0


    def tick(self):
        if self.game.gameover == False:
            if self.pos.y > 520.0:
                self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 80), -random.randint(200, 400))
                self.rect.x = self.pos.x
                self.rect.y = self.pos.y
            else:
                self.pos -= Vector2(0, -self.gravity-self.speed)
                self.rect.x = self.pos.x
                self.rect.y = self.pos.y


    def draw(self):
        self.game.screen.blit(self.image, [self.pos.x, self.pos.y])


class Rock2(object):
    def __init__(self,game):
        self.game = game
        self.image = pygame.image.load("upload\\objects\\rock2.png")
        self.rect = self.image.get_rect()
        self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 79), -random.randint(200, 400))
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.gravity = self.game.gravity
        self.speed = 0.3
        self.object_delta = 0.0
        self.speed_down = 60.0


    def tick(self):
        if self.game.gameover == False:
            if self.pos.y > 520.0:
                self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 80), -random.randint(200, 400))
                self.rect.x = self.pos.x
                self.rect.y = self.pos.y
            else:
                self.pos -= Vector2(0, -self.gravity-self.speed)
                self.rect.x = self.pos.x
                self.rect.y = self.pos.y


    def draw(self):
        self.game.screen.blit(self.image, [self.pos.x, self.pos.y])

class Rock3(object):
    def __init__(self,game):
        self.game = game
        self.image = pygame.image.load("upload\\objects\\rock3.png")
        self.rect = self.image.get_rect()
        self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 79), -random.randint(200, 400))
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.gravity = self.game.gravity
        self.speed = 0.3
        self.object_delta = 0.0
        self.speed_down = 80.0


    def tick(self):
        if self.game.gameover == False:
            if self.pos.y > 520.0:
                self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 80), -random.randint(200, 400))
                self.rect.x = self.pos.x
                self.rect.y = self.pos.y
            else:
                self.pos -= Vector2(0, -self.gravity-self.speed)
                self.rect.x = self.pos.x
                self.rect.y = self.pos.y


    def draw(self):
        self.game.screen.blit(self.image, [self.pos.x, self.pos.y])

class Rock4(object):
    def __init__(self,game):
        self.game = game
        self.image = pygame.image.load("upload\\objects\\rock4.png")
        self.rect = self.image.get_rect()
        self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 79), -random.randint(200, 400))
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.gravity = self.game.gravity
        self.speed = 0.3
        self.object_delta = 0.0
        self.speed_down = 70.0


    def tick(self):
        if self.game.gameover == False:
            if self.pos.y > 520.0:
                self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 80), -random.randint(200, 400))
                self.rect.x = self.pos.x
                self.rect.y = self.pos.y
            else:
                self.pos -= Vector2(0, -self.gravity-self.speed)
                self.rect.x = self.pos.x
                self.rect.y = self.pos.y


    def draw(self):
        self.game.screen.blit(self.image, [self.pos.x, self.pos.y])
