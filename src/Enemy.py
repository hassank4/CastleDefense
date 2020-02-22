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
        # The list of pixels where the Enemy will have to go to (1000x600)
        self.points = [(258, 595), (236, 524), (141, 488), (82, 420), (111, 329), (232, 282), (270, 150), (341, 114), (498, 114), (566, 172), (566, 373), (615, 441), (984, 441)]
        # The index of the Enemy's current point from the list of points
        self.current = 0

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

    def getPosition(self):  # Function to get the Enemy position
        return self.points[self.current]

    def moveToNextPoint(self): # Function to move through points in self.points and return a tuple of X and Y changes
        # Checking if the Enemy is already at the last point
        if (self.current == (len(self.points) - 1)):
            return (0, 0)
        else:
            self.current += 1
            return ((self.points[self.current])[0] - (self.points[self.current - 1])[0], (self.points[self.current])[1] - (self.points[self.current - 1])[1])
