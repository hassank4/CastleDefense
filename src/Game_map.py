import pygame
import os
import random
from Assassin import Assassin
from Mage import Mage
from Ogre import Ogre

pygame.font.init()

# from src.Enemy import Enemy
pygame.init()

waves = [[5, 0, 0], [0, 5, 0], [0, 0, 5]]
currency_img = pygame.image.load(os.path.join("images", "crystal_1.png"))

WIDTH = 1000
HEIGHT = 600


class Game_map:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 10
        self.money = 250
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.background = pygame.image.load(os.path.join("images", "temp_background.png"))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        self.enemies.append(random.choice([Mage(0), Assassin(0), Ogre(0)]))
        while run:
            clock.tick(100)
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
        #    enemy_groups = [Mage(0), Assassin(0), Ogre(0)]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
         #           self.enemies.append(enemy_groups[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    def draw(self):
        self.win.blit(self.background, (0, 0))
        '''
        # display enemies
        for enemy in self.enemies:
            enemy.draw(self.win)
        '''
        for enemy in self.enemies:
            enemy.draw(self.win)
            if enemy.getPosition() == (0,0):
                del enemy
                
            #enemy.getPosition()
        # display currency
        '''
        text = self.life_font.render(str(self.money), 1, (255, 255, 255))
        money = pygame.transform.scale(coins_img, (50, 50))
        start_x = self.width - life.get_width() - 10
        '''
        pygame.display.update()


g = Game_map()
g.run()
