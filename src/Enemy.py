"""
This class is for the Enemy object. This class allows us to keep track of
an Enemy's id as well as it's health. An Enemy can lose its health.
The health of an Enemy can be as high as 1000 or as low as 0.
"""

class Enemy:
    def __init__(self, id, image): # Constructor to create an Enemy object
        self.id = id
        self.health = 100
        self.image = image
        # The initial point
        self.initial = (497, 2070)
        # The list of pixels where the Enemy will have to go to
        self.points = [(395, 905), (255, 873), (179, 807), (156, 686), (236, 576), (341, 543), (450, 497), (495, 393), (516, 293), (635, 209), (951, 206), (1091, 332), (1092, 657), (1181, 786), (1899, 786)]

    def __str__(self): # Function to output Enemy health
        return "Enemy " + str(self.id) + ": " + str(self.health) + " Health"

    def getHealth(self): # Function to get the Enemy health
        return self.health

    def getId(self): # Function to get the Enemy id
        return self.id

    def subHealth(self, amount): # Function to deduct Enemy health
        self.health = self.health - amount
        if(self.health < 0):
            self.health = 0

    def movePath(self): # Function to move through points in self.points
        pass
