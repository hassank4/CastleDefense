from Enemy import Enemy
from Tower import Tower

class Mage(Enemy):
    def __init__(self, id): # Constructor to create an Enemy object
        Enemy.__init__(self, id, "Images\mage_walk.png", "Images\mage_attack.png")
        self.speed = 3

    def __str__(self): # Function to output Enemy health
        return "Mage " + str(self.id) + ": " + str(self.health) + " Health"
    
    def attack(self, tower):
        tower.take_damage(4)
        
