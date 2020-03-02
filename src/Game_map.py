import pygame
import os
from src.Assassin import Assassin
from src.Knight import WeakKnight
from src.Archer import WeakArcher
from src.Wizard import WeakWizard
from src.Mage import Mage
from src.Ogre import Ogre
from src.Menu import Purchase_Menu

pygame.font.init()
pygame.init()

# images
currency_img = pygame.transform.scale(pygame.image.load(os.path.join("images", "crystal_1.png")), (20, 20))
menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("images", "window_1.png")), (400, 110))
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
        self.i = 0
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 10
        self.money = 1000
        self.wave = 0
        self.moving_object = None
        self.current_wave = waves[self.wave][:]
        self.background = pygame.image.load(os.path.join("images", "temp_background.png"))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.menu = Purchase_Menu(self.width - 200, self.height + 7, menu_bg)
        self.menu.add_btn(buy_archer1, "buy_archer1", 200)
        self.menu.add_btn(buy_knight1, "buy_knight1", 300)
        self.menu.add_btn(buy_wizard1, "buy_wizard1", 400)

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(500)
            # self.create_enemy()

            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    purchase_button = self.menu.get_clicked(mouse_pos[0], mouse_pos[1])
                    if purchase_button:
                        print(purchase_button)

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

        text = pygame.font.SysFont("comicsans", 40).render(str(self.money), 1, (0, 0, 0))
        money = pygame.transform.scale(currency_img, (25, 25))

        self.win.blit(text, (5, 1))
        self.win.blit(money, (80, 3))

        # draw menu
        self.menu.draw(self.win)
        pygame.display.update()

    def add_defense(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_archer1", "buy_knight1", "buy_wizard1"]
        object_list = [WeakArcher(self.i, x, y), WeakKnight(self.i, x, y), WeakWizard(self.i, x, y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
            self.i = self.i + 1
        except Exception as e:
            print(str(e) + "NOT VALID NAME")


g = Game_map()
g.run()
