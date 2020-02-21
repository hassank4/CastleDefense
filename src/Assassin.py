"""
This class is for the Enemy object. This class allows us to keep track of
an Enemy's id as well as it's health. An Enemy can lose its health.
The health of an Enemy can be as high as 1000 or as low as 0.
"""
from Enemy import Enemy
from Tower import Tower

class Assassin(Enemy):
    def __init__(self, id): # Constructor to create an Enemy object
        Enemy.__init__(self, id, "Images\assassin_walk.png")
        self.health = 80

    def __str__(self): # Function to output Enemy health
        return "Knight " + str(self.id) + ": " + str(self.health) + " Health"

    def attack(self, tower):
        tower.take_damage(2)
