from src.Menu import Menu
import pygame
import os

menu_backg = pygame.transform.scale(pygame.image.load(os.path.join("images", "window_1.png")), (400, 110))

class Tower:
    """
    The class for a Tower. Takes a path for the graphic and starts the Tower off with 100 health.
    """
    def __init__(self, img_path):
        """Initialize a Tower."""
        self.health = 100
        self.img_path = img_path
        self.menu = Menu(self, 790, 210, menu_backg, [2000, "MAX"])
        self.selected = False

    def __str__(self):
        """Return a string representation of Tower's health."""
        return "Health: " + str(self.health)

    def get_health(self):
        """Return Tower's HP."""
        return self.health

    def take_damage(self, amount):
        """Take a damage amount and deduct it from the Tower's health."""
        # Ensure Tower's health is non-negative.
        if self.health > amount:
            self.health -= amount
        else:
            self.health = 0

    def click(self, X, Y):
        """Returns if tower has been clicked on and selects tower if it was clicked"""

        img = self.img_path
        if 790 - img.get_width() // 2 + self.width >= X >= 790 - img.get_width() // 2:
            if 210 + self.height - img.get_height() // 2 >= Y >= 210 - img.get_height() // 2:
                return True
        return False

    def draw(self, win):
        """Draw the tower onto the map"""
        img = self.img_path
        win.blit(img, (790, 210))

        # draw menu
        if self.selected:
            self.menu.draw(win)

