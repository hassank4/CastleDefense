import pygame
import os

pygame.init()
pygame.font.init()

currency_img = pygame.transform.scale(pygame.image.load(os.path.join("images", "crystal_1.png")), (60, 60))
currency_img2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "crystal_1.png")), (20, 20))

health_icon = pygame.transform.scale(pygame.image.load(os.path.join("images", "zip.png")), (10, 10))


class Button:
    def __init__(self, menu, img, label):
        self.label = label
        self.img = img
        self.x = menu.x + 75
        self.y = menu.y - 103
        self.menu = menu
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def click(self, X, Y):
        if self.x + self.width >= X >= self.x:
            if self.y + self.height >= Y >= self.y:
                return True
        return False

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def update(self):
        self.x = self.menu.x
        self.y = self.menu.y



'''
This class will be used for creating menus 
'''


class Menu:
    def __init__(self, tower, x, y, img, price):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.price = price
        self.buttons = []
        self.items = 0
        self.background = img
        self.font = pygame.font.SysFont("comicsans", 25)
        self.tower = tower

    def add_btn(self, img, name):
        self.items += 1
        self.buttons.append(Button(self, img, name))

    def edit_btn(self, img, name):
        self.buttons.clear()
        self.buttons.append(Button(self, img, name))

    def get_item_cost(self):
        return self.price[self.tower.level - 1]

    def draw(self, win):
        win.blit(self.background, (self.x + self.background.get_width() / 2, self.y - 110))
        for item in self.buttons:
            item.draw(win)
            win.blit(health_icon, (item.x - 10, item.y ))

    def get_clicked(self, x1, y1):
        for button in self.buttons:
            if button.click(x1, y1):
                return button.name

        return None

    def update(self):
        for button in self.buttons:
            button.update()


class Menu2_Button(Button):
    def __init__(self, x, y, img, name, cost):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.cost = cost


class Purchase_Menu(Menu):
    """
    Menu at the bottom of the game where defenses and their prices will be displayed
    """

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont("comicsans", 25)

    def add_btn(self, img, name, cost):
        self.items += 1
        btn_x = self.x - 100 + (self.items - 1) * 130
        btn_y = self.y - 110
        self.buttons.append(Menu2_Button(btn_x - 30, btn_y, img, name, cost))

    def get_item_cost(self, name):
        """
        gets cost of item
        :param name: str
        :return: int
        """
        for btn in self.buttons:
            if btn.name == name:
                return btn.cost
        return -1

    def draw(self, win):
        """draws purchase menu at the bottom"""
        win.blit(self.bg, (self.x - self.bg.get_width() / 2, self.y - 120))
        for item in self.buttons:
            item.draw(win)
            win.blit(currency_img2, (item.x + 2, item.y + item.height + 3))
            text = self.font.render(str(item.cost), 1, (255, 255, 255))
            win.blit(text, (item.x + item.width / 2 - text.get_width() / 2 + 10, item.y + item.height + 3))
