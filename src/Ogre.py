from Enemy import Enemy
from Tower import Tower
import pygame
import os

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'Images') # The resource folder path
image_path = os.path.join(resource_path, 'ogre') # The image folder path

class Ogre(Enemy):
    def __init__(self, id): # Constructor to create an Enemy object
        Enemy.__init__(self, id)
        self.health = 200
        self.speed = 1
        image = [pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'walk1.png')).convert_alpha(), (64, 64))]
        self.image = image

    def __str__(self): # Function to output Enemy health
        return "Tank " + str(self.id) + ": " + str(self.health) + " Health"

    def attack(self, tower):
        tower.take_damage(7)
        

