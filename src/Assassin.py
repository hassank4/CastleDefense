from Enemy import Enemy
from Tower import Tower

class Assassin(Enemy):
    def __init__(self, id): # Constructor to create an Enemy object
        Enemy.__init__(self, id, "Images\assassin_walk.png", "Images\assassin_attack.png")
        self.health = 80
        self.speed = 5

    def __str__(self): # Function to output Enemy health
        return "Assassin " + str(self.id) + ": " + str(self.health) + " Health"

    def attack(self, tower):
        tower.take_damage(2)
