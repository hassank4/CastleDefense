import pygame
import os
import random
pygame.init()

"""
This class displays the start screen to the user when they decide to play the game.
"""


class Start():

        # Constructor
        def __init__(self):
                self.width = 1200
                self.height = 800
                self.win = pygame.display.set_mode((self.width, self.height))
                self.background = pygame.image.load(os.path.join("Images/Start-Screen2.png"))
                self.background = pygame.transform.scale(self.background, (self.width, self.height))                  
        
        # Method to display the start screen
        def draw(self):
                self.win.blit(self.background, (0,0))
                pygame.display.update()

        # Method to display the screen until the user wants to quit
        def done(self):
                done = True
                clock = pygame.time.Clock()     
                while done:
                        clock.tick(60)
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        done = False 

                        self.draw()
                pygame.quit()

s = Start()
s.done()

