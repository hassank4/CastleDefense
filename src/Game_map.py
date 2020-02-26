import pygame
import os
import random
pygame.init()

WIDTH = 1000
HEIGHT = 600
class Game_map:

        def __init__(self):
                self.width = WIDTH
                self.height = HEIGHT
                self.win = pygame.display.set_mode((self.width, self.height))
                self.enemies = []
                self.towers = []
                self.lives = 10
                self.money = 250
                self.background = pygame.image.load(os.path.join("images", "temp_background.png"))
                self.background = pygame.transform.scale(self.background, (self.width, self.height))                  
                #self.clicks = [] #Mouse clicks
        def done(self):
                done = True
                clock = pygame.time.Clock()     
                while done:
                        clock.tick(60)
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        done = False 
                                #Get the position of mouse clicks- will be used to know where enemies should travel in a path
                                #pos = pygame.mouse.get_pos()

                                #if event.type == pygame.MOUSEBUTTONDOWN:
                                        #self.clicks.append(pos)
                                        #print(pos)

                        self.draw()

                pygame.quit()

        def draw(self):
                self.win.blit(self.background, (0,0))
                #for p in self.clicks:
                        #pygame.draw.circle(self.win, (255,0,0), (p[0] , p[1]), 5, 0)
                pygame.display.update()

g = Game_map()
g.done()



