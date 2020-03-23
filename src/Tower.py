from src.Menu import Menu
import pygame
import os

menu_backg = pygame.transform.scale(pygame.image.load(os.path.join("images", "window_1.png")), (120, 30))
tower_health_bar = pygame.transform.scale(pygame.image.load(os.path.join("images", "health_bar-06.png")), (100, 10))


class Tower:
    """
    The class for a Tower. Takes a path for the graphic and starts the Tower off with 100 health.
    """
    def __init__(self, img_path):
        """Initialize a Tower."""
        self.health = 100
        self.img_path = img_path
        self.menu2 = Menu(self, 770, 280, menu_backg, 0)
        self.menu2.add_btn(tower_health_bar, "tower health")

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
        if 790 <= X <= 790 + img.get_width():
            if 210 <= Y <= 210 + img.get_height():
                return True
        return False

    def draw(self, win):
        """Draw the tower onto the map"""
        img = self.img_path
        win.blit(img, (790, 210))

        # draw menu
        if self.selected:
            self.menu2.draw(win)

