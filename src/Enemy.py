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
        self.points = [(258, 595), (236, 524), (141, 488), (82, 420), (111, 329), (232, 282), (270, 150), (341, 114), (498, 114), (566, 172), (566, 373), (615, 441), (984, 441)]
        # The index of the Enemy's current point from the list of points
        self.current = 0
        self.image = []
        self.count = 0
        self.speed = 0
        self.x = 258
        self.y = 595

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


    def draw(self, win):
        i = self.image[self.count]
        win.blit(i, (self.getPosition()[0] - i.get_width()/2, self.getPosition()[1] - i.get_height()/2 - 35))
        change = self.moveToNextPoint()
        slope = change[1]//change[0]
        if (slope < 0):
            self.x += 1
        else:
            self.x -= 1
        self.y -= slope
        rangex = []
        for i in range((self.points[self.current + 1])[0] - 4, (self.points[self.current + 1])[0] + 4):
            rangex.append(i)
        rangey = []
        for i in range((self.points[self.current + 1])[1] - 4, (self.points[self.current + 1])[1] + 4):
            rangey.append(i)
        if ((self.x in rangex) and (self.y in rangey)):
            self.current += 1
            self.count += 1
        
        
    def moveToNextPoint(self): # Function to move through points in self.points and return a tuple of X and Y changes
        # Checking if the Enemy is already at the last point
        if (self.current == 12):
            return (0, 0)
        else:
            # self.current = self.current + 1
            return (self.points[self.current + 1][0] - self.points[self.current][0], self.points[self.current + 1][1] - self.points[self.current][1])
