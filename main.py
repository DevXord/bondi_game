import pygame, sys, random, bondi,ground,food,rock


class My_Game(object):
    def __init__(self):
        self.tps_max = 100.0
        self.gravity = 0.6
        pygame.init()
        self.last_player_score = 0
        self.gameover = False
        self.screen = pygame.display.set_mode((1280, 640))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.ground = ground.Ground(self.screen)
        self.player = bondi.Bondi(self)
        self.objects = [food.Coce(self),
                        food.Pepo(self),
                        food.Pizza(self),
                        food.Hambuerger(self),
                        food.Hotdog(self)]
        self.objects_rock = [rock.Rock(self),
                            rock.Rock2(self),
                            rock.Rock3(self),
                            rock.Rock4(self)]


        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit(0)
            keys = pygame.key.get_pressed()
            if self.gameover and keys[pygame.K_RETURN]:
                self.last_player_score = 0
                self.gameover = False
                self.reset_game()
            else:
                self.tps_delta += self.tps_clock.tick() / 1000.0
                for o in self.objects:
                    o.object_delta += self.tps_clock.tick() / 1000.0
                    if self.player.rect.colliderect(o.rect):
                        o.pos = pygame.Vector2(random.randint(0, self.screen.get_width() - 80), -random.randint(20, 200))
                        o.rect.x = o.pos.x
                        o.rect.y = o.pos.y
                        self.player.player_score += o.score

                for r in self.objects_rock:
                    r.object_delta += self.tps_clock.tick() / 1000.0
                    if self.player.rect.colliderect(r.rect):
                        self.gameover = True
                        for p in self.objects:
                            p.gravity = 0.0
                            p.speed = 0.0
                        for r in self.objects_rock:
                            r.gravity = 0.0
                            r.speed = 0.0
                        self.gravity = 0.0


                while self.tps_delta > 1/self.tps_max:
                    if self.gameover == False:
                        for o in self.objects:
                            if o.object_delta > 1 / o.speed_down:
                                o.speed += 0.1
                                o.object_delta -= 1 / o.speed_down
                        for r in self.objects_rock:
                            if r.object_delta > 1 / r.speed_down:
                                r.speed += 0.1
                                r.object_delta -= 1 / r.speed_down
                        self.tick()
                    self.tps_delta -= 1/self.tps_max

                if self.gameover == False:
                    self.screen.fill((104, 147, 255))
                else:
                    self.screen.fill((0,0,0))

            self.draw()
            pygame.display.flip()


    def reset_game(self):
        for p in self.objects:
            p.pos = pygame.Vector2(random.randint(0, self.screen.get_width() - 79), -random.randint(200, 400))
            p.rect.x = p.pos.x
            p.rect.y = p.pos.y
            p.object_delta = 0.0
            p.gravity = 0.6
            p.speed = 0.1

        for r in self.objects_rock:
            r.pos = pygame.Vector2(random.randint(0, self.screen.get_width() - 79), -random.randint(200, 400))
            r.rect.x = r.pos.x
            r.rect.y = r.pos.y
            r.object_delta = 0.0
            r.gravity = 0.6
            r.speed = 0.1
        self.last_player_score = self.player.player_score
        self.player.player_score = 0
        self.gravity = 0.6



    def tick(self):

        self.player.tick()
        for p in self.objects:
            p.tick()

        for r in self.objects_rock:
             r.tick()



    def draw(self):

        if self.gameover == False:
            self.player.draw()
            self.ground.draw()
            my_ft_font = pygame.freetype.SysFont('Times New Roman', 32)
            my_ft_font.render_to(self.screen, (self.screen.get_width() * 0.46, 10), "Score: " + str(self.player.player_score), (0, 0, 0))
            for p in self.objects:
                p.draw()
            for r in self.objects_rock:
                r.draw()
        else:
            my_ft_font = pygame.freetype.SysFont('Times New Roman', 32)
            my_ft_font.render_to(self.screen, (self.screen.get_width() * 0.43, self.screen.get_height() * 0.26),"GAME OVER",(179, 0, 3))
            my_ft_font.render_to(self.screen, (self.screen.get_width() * 0.43, self.screen.get_height() * 0.36),"Your Score: "+str(self.last_player_score),(179, 0, 3))
            my_ft_font.render_to(self.screen, (self.screen.get_width() * 0.35, self.screen.get_height() * 0.46),"Press Enter to continue the game", (179, 0, 3))


if __name__ == "__main__":
    My_Game()
