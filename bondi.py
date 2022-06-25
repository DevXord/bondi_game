import pygame
from  pygame.math import Vector2

class Bondi(object):
    def __init__(self,game):
        self.playerimg = None
        self.jump = self.left = self.right = False
        self.jumpspeed = 15.0
        self.player_score = 0
        self.image = pygame.image.load("upload\\player\\stay.png" )
        self.rect = self.image.get_rect()
        self.game = game
        self.pos = Vector2(0,300)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.speed = 0.5
        self.air_resistance = 0.8
        self.gravity = self.game.gravity

    def add_pos(self,force):
        self.acc += force

    def tick(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if self.pos.x > 1.0:
                self.add_pos(Vector2(-self.speed, self.acc.y))
                self.left = True
                self.right = False
        elif keys[pygame.K_d]:
            if self.pos.x < self.game.screen.get_width() - 80:
                self.add_pos(Vector2(self.speed, self.acc.y))
                self.left = False
                self.right = True
        else:
            self.left = False
            self.right = False

        if keys[pygame.K_SPACE] and self.jump == False:
            self.add_pos(Vector2(self.acc.x, -self.jumpspeed))
            self.jump = True







        self.vel *= self.air_resistance
        if self.rect.colliderect(self.game.ground.rect):
            self.image = pygame.image.load("upload\\player\\stay.png")
            self.rect = self.image.get_rect()
            self.jump = False
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
        else:
            self.vel -= Vector2(0,-self.gravity)
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0





    def draw(self):

        if self.left:
            self.image = pygame.image.load("upload\\player\\left.png")
        elif self.right:
            self.image = pygame.image.load("upload\\player\\right.png")
        if self.jump:
            self.image = pygame.image.load("upload\\player\\jump.png")


        self.playerimg = self.image
        self.game.screen.blit(self.playerimg, [self.pos.x,self.pos.y])
