"""
This class is for the Enemy object. This class allows us to keep track of
an Enemy's id as well as it's health. An Enemy can lose its health.
The health of an Enemy can be as high as 1000 or as low as 0.
"""
import pygame
import math
import os
import random

class Enemy:
    def __init__(self, id): # Constructor to create an Enemy object
        self.id = id
        self.health = 100
        # The list of pixels where the Enemy will have to go to (1000x600)
        self.points = [(260, 593), (238, 526), (131, 492), (80, 441), (106, 336), (130, 332), (238, 290), (259, 189), (300, 121), (414, 116), (532, 121), (548, 148), (570, 195), (576, 400), (630, 441), (986, 446)]
        # The index of the Enemy's current point from the list of points
        self.current = 0
        self.image = []
        self.count = 0
        self.speed = 0
        self.x = 260
        self.y = 593

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

    def getPosition(self):  # Function to get the Enemy position
        # return self.points[self.current]
        return (self.x, self.y)

    def slide(self):
        if self.current + 1 >= len(self.points):
            self.x, self.y = (0,0)
        else:
            change = self.moveToNextPoint()
            x2, y2 = self.points[self.current+1]

            length = math.sqrt((change[0])**2 + (change[1])**2)
            change = (change[0]/length, change[1]/length)

            self.x = self.x + change[0]
            self.y = self.y + change[1]

            if change[0] >= 0: # right
                if change[1] >= 0: # down
                    if self.x >= x2+5 and self.y >= y2:
                        self.current += 1
                else:
                    if self.x >= x2+5 and self.y <= y2:
                        self.current += 1
            else: # left
                if change[1] >= 0:  # down
                    if self.x <= x2+5 and self.y >= y2:
                        self.current += 1
                else:
                    if self.x <= x2+5 and self.y >= y2:
                        self.current += 1

    def draw(self, win):
        i = self.image[self.count]
        win.blit(i, (self.getPosition()[0] - i.get_width()/2, self.getPosition()[1] - i.get_height()/2 - 35))
        
        self.slide()
        
        
    def moveToNextPoint(self): # Function to move through points in self.points and return a tuple of X and Y changes
        # Checking if the Enemy is already at the last point
        if (self.current == len(self.points)):
            return (0, 0)
        else:
            # self.current = self.current + 1
            return (self.points[self.current + 1][0] - self.points[self.current][0], self.points[self.current + 1][1] - self.points[self.current][1])
