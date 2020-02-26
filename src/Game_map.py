import pygame
import os
from src.Enemy import Assassin
from src.Enemy import Mage
from src.Enemy import Ogre

# from src.Enemy import Enemy
pygame.init()

waves = [[5, 0, 0], [0, 5, 0], [0, 0, 5]]


class Game_map:
    def __init__(self):
        self.width = 1000
        self.height = 600
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 10
        self.money = 250
        self.background = pygame.image.load(os.path.join("images", "temp_background.png"))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.wave = 0
        self.current_wave = waves[self.wave][:]

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                else:
                    self.create_enemy()
            self.draw()

        pygame.quit()

    def create_enemy(self):
        if sum(self.current_wave) == 0:
            if len(self.enemies) == 0:
                self.wave += 1
                self.current_wave = waves[self.wave]

        else:
            enemy_groups = [Assassin(), Mage(), Ogre()]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemies.append(enemy_groups[x])
                    self.current_group[x] = self.current_group[x] - 1
                    break

    def draw(self):
        self.win.blit(self.background, (0, 0))
        # for p in self.clicks:
        # pygame.draw.circle(self.win, (255,0,0), (p[0] , p[1]), 5, 0)
        pygame.display.update()


g = Game_map()
g.run()
