import pygame, random
from  pygame.math import Vector2

class Coce(object):
    def __init__(self,game):
        self.game = game
        self.score = 8
        self.image = pygame.image.load("upload\\objects\\coce.png")
        self.rect = self.image.get_rect()
        self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 79), -random.randint(20, 200))
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.gravity = 0.6
        self.speed = 0.1
        self.object_delta = 0.0
        self.speed_down = 10.0

    def tick(self):
        if self.pos.y > 520.0 :
            self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 80), -random.randint(20, 200))
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
        else:
            self.pos -= Vector2(0, -self.gravity - self.speed)
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y



    def draw(self):
        self.game.screen.blit(self.image, [self.pos.x, self.pos.y])



class Hambuerger():
    def __init__(self,game):
        self.game = game
        self.score = 6
        self.image = pygame.image.load("upload\\objects\\hamburger.png")
        self.rect = self.image.get_rect()
        self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 79), -random.randint(20, 200))
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.gravity = self.game.gravity
        self.speed = 0.1
        self.object_delta = 0.0
        self.speed_down = 60.0

    def tick(self):
        if self.pos.y > 520.0:
            self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 80), -random.randint(20, 200))
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
        else:
            self.pos -= Vector2(0, -self.gravity - self.speed)
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y


    def draw(self):
        self.game.screen.blit(self.image, [self.pos.x, self.pos.y])


class Hotdog(object):
    def __init__(self,game):
        self.game = game
        self.score = 3
        self.image = pygame.image.load("upload\\objects\\hotdog.png")
        self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 79), -random.randint(20, 200))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

        self.gravity = self.game.gravity
        self.speed = 0.1
        self.object_delta = 0.0
        self.speed_down = 60.0

    def tick(self):
        if self.rect.y > 520.0:
            self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 80), -random.randint(20, 200))
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y


        else:
            self.pos -= Vector2(0, -self.gravity - self.speed)
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y


    def draw(self):
        self.game.screen.blit(self.image, self.pos)



class Pepo(object):
    def __init__(self,game):
        self.game = game
        self.score = 2
        self.image = pygame.image.load("upload\\objects\\pepo.png")
        self.rect = self.image.get_rect()
        self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 79), -random.randint(20, 200))
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.gravity = self.game.gravity
        self.speed = 0.1
        self.object_delta = 0.0
        self.speed_down = 30.0

    def tick(self):
        if self.pos.y > 520.0:
            self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 80), -random.randint(20, 200))
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
        else:
            self.pos -= Vector2(0, -self.gravity - self.speed)
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y

    def draw(self):
        self.game.screen.blit(self.image, [self.pos.x, self.pos.y])

class Pizza(object):
    def __init__(self,game):
        self.game = game
        self.score = 5
        self.image = pygame.image.load("upload\\objects\\pizza.png")
        self.rect = self.image.get_rect()
        self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 79), -random.randint(20, 200))
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.gravity = self.game.gravity
        self.speed = 0.1
        self.object_delta = 0.0
        self.speed_down = 50.0


    def tick(self):
        if self.pos.y > 520.0:
            self.pos = Vector2(random.randint(0, self.game.screen.get_width() - 80), -random.randint(20, 200))
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
        else:
            self.pos -= Vector2(0, -self.gravity-self.speed)
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y


    def draw(self):
        self.game.screen.blit(self.image, [self.pos.x, self.pos.y])
