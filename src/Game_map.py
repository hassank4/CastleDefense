import pygame
import os
from src.Assassin import Assassin
from src.Mage import Mage
from src.Ogre import Ogre
from src.Menu import Purchase_Menu

pygame.font.init()
pygame.init()

# images
currency_img = pygame.transform.scale(pygame.image.load(os.path.join("images", "crystal_1.png")), (20, 20))
menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("images", "window_1.png")), (500, 110))
buy_archer1 = pygame.transform.scale(pygame.image.load(os.path.join("images/defense/archer1/idle1.png")), (75, 75))

buy_knight1 = pygame.transform.scale(pygame.image.load(os.path.join("images/defense/knight1/idle1.png")), (75, 75))

buy_wizard1 = pygame.transform.scale(pygame.image.load(os.path.join("images/defense/wizard1/idle1.png")), (75, 75))

WIDTH = 1000
HEIGHT = 600

waves = [[5, 0, 0], [0, 5, 0], [0, 0, 5]]


class Game_map:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 10
        self.money = 1000
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.background = pygame.image.load(os.path.join("images", "temp_background.png"))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.menu = Purchase_Menu(self.width - 250, self.height + 7, menu_bg)
        self.menu.add_btn(buy_archer1, "buy_archer1", 200)
        self.menu.add_btn(buy_knight1, "buy_knight1", 300)
        self.menu.add_btn(buy_wizard1, "buy_wizard1", 400)

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(500)
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
            enemy_groups = [Assassin(0), Mage(0), Ogre(0)]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemies.append(enemy_groups[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    def draw(self):
        self.win.blit(self.background, (0, 0))

        '''
        # display enemies
        for enemy in self.enemies:
            enemy.draw(self.win)
        '''
        # display currency

        text = pygame.font.SysFont("comicsans",40).render(str(self.money), 1, (255, 255, 255))
        money = pygame.transform.scale(currency_img, (10, 10))

        self.win.blit(text, (900, 75))
        self.win.blit(money, (850, 65))

        # draw menu
        self.menu.draw(self.win)
        pygame.display.update()


g = Game_map()
g.run()
