import math, random, sys
import pygame
from pygame.locals import *

# define display surface                        
W, H = 500, 500
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Sprite Sheets")
FPS = 10

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

#REFRENCE: https://www.youtube.com/watch?v=mfX3XQv9lnI
class Spritesheet:
        def __init__(self, filename, cols, rows):
                self.sheet = pygame.image.load(filename).convert_alpha()
                
                self.cols = cols
                self.rows = rows
                self.totalCellCount = cols * rows
                
                self.rect = self.sheet.get_rect()
                self.cellWidth = int(self.rect.width / cols)
                self.cellHeight = int(self.rect.height / rows)
                hw, hh = self.cellCenter = (int(self.cellWidth / 2), int(self.cellHeight / 2))
                
                self.cells = list([(index % cols * self.cellWidth, int(index / cols) * self.cellHeight, self.cellWidth, self.cellHeight)
                                   for index in range(self.totalCellCount)])
                
                self.handle = list([
                        (0, 0), (-hw, 0), (-self.cellWidth, 0),
                        (0, -hh), (-hw, -hh), (-self.cellWidth, -hh),
                        (0, -self.cellHeight), (-hw, -self.cellHeight), (-self.cellWidth, -self.cellHeight),])
                
        def draw(self, surface, cellIndex, x, y, handle = 0):
                surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])

        def file_change(self, filename):
                self.sheet = pygame.image.load(filename).convert_alpha()

#TESTING

s = Spritesheet("Images\assassin_attack.png", 3, 2)

CENTER_HANDLE = 4

index = 0
count = 0
# main loop
while True:

        s.draw(DS, index % s.totalCellCount, HW, HH, 4)
        index += 1
        
        if(count == 10):
                s.file_change("Images\assassin_attack.png")
        
        count = count + 1
        pygame.display.update()
        CLOCK.tick(FPS)
        DS.fill(BLACK)
