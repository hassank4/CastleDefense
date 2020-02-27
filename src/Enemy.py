"""
This class is for the Enemy object. This class allows us to keep track of
an Enemy's id as well as it's health. An Enemy can lose its health.
The health of an Enemy can be as high as 1000 or as low as 0.
"""

class Enemy:
    def __init__(self, id, walk_image, attack_image): # Constructor to create an Enemy object
        self.id = id
        self.health = 100
        self.walk_image = walk_image
        self.attack_image = attack_image
        self.speed = 0

    def __str__(self): # Function to output Enemy health
        return "Enemy " + str(self.id) + ": " + str(self.health) + " Health"

    def getHealth(self): # Function to get the Enemy health
        return self.health

    def getId(self): # Function to get the Enemy id
        return self.id

    def getSpeed(self): # Function to get the Enemy id
        return self.speed
    
    def subHealth(self, amount): # Function to deduct Enemy health
        self.health = self.health - amount
        if(self.health < 0):
            self.health = 0
