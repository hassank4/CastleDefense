from Enemy import Enemy
from Tower import Tower
import pygame
import os

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'Images') # The resource folder path
image_path = os.path.join(resource_path, 'assassin') # The image folder path

class Assassin(Enemy):
    def __init__(self, id): # Constructor to create an Enemy object
        Enemy.__init__(self, id)
        self.health = 80
        self.speed = 5
        image = []
        for i in range(5):
            image.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'walk' + str(i+1)+ '.png')).convert_alpha(), (64, 64)))
        self.image = image

    def __str__(self): # Function to output Enemy health
        return "Assassin " + str(self.id) + ": " + str(self.health) + " Health"

    def attack(self, tower):
        tower.take_damage(2)
