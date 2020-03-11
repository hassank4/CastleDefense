import pygame
import time
import random
 
pygame.init()

display_width = 1000
display_height = 600
 
black = (0,0,0)
white = (255,255,255)

red = (180,0,0)
green = (0,180,0)
blue = (0,0,180)
yellow = (200, 200, 31)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)
bright_yellow = (255, 255, 51)
 
block_color = (53,115,255)

# --------------------------------------------------------------------------------------------
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Castle Defense')
clock = pygame.time.Clock()
 
backgroundImg = pygame.image.load('Images/Start-Screen2.png')

pause = False 

# --------------------------------------------------------------------------------------------
 

def make_button(message, x, y, width, height, active_col, inactive_col, action):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_col, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()
           
    else:
        pygame.draw.rect(gameDisplay, inactive_col, (x, y, width, height))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(message, smallText)
    textRect.center = ((x + (width/2)), (y + (height/2)))
    gameDisplay.blit(textSurf, textRect)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
    time.sleep(2)
 

def helpmenu1():
    help = True

    while help:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',75)
        TextSurf, TextRect = text_objects("Help Menu 1", largeText)
        TextRect.center = ((display_width/2),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)

        make_button("Next", 10, 500, 150, 50, bright_yellow, yellow, helpmenu2)
        make_button("Quit", 810, 30, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def helpmenu2():
    help = True

    while help:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',75)
        TextSurf, TextRect = text_objects("Help Menu 2", largeText)
        TextRect.center = ((display_width/2),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)

        make_button("Next", 210, 500, 150, 50, bright_yellow, yellow, helpmenu3)
        make_button("Quit", 810, 30, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def helpmenu3():
    help = True

    while help:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',75)
        TextSurf, TextRect = text_objects("Help Menu 3", largeText)
        TextRect.center = ((display_width/2),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)

        make_button("Next", 410, 500, 150, 50, bright_yellow, yellow, helpmenu4)
        make_button("Quit", 810, 30, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def helpmenu4():
    help = True

    while help:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',75)
        TextSurf, TextRect = text_objects("Help Menu 4", largeText)
        TextRect.center = ((display_width/2),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)

        make_button("Next", 610, 500, 150, 50, bright_yellow, yellow, helpmenu5)
        make_button("Quit", 810, 30, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def helpmenu5():
    help = True

    while help:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',75)
        TextSurf, TextRect = text_objects("Help Menu 5", largeText)
        TextRect.center = ((display_width/2),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)

        make_button("Back to Main", 810, 500, 150, 50, bright_yellow, yellow, start)
        make_button("Quit", 810, 30, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)


def gameloop():
    global pause
    gameloop = True

    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Game Map", largeText)
        TextRect.center = ((display_width/5),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)

        
        make_button("Game End", 800, 50, 150, 50, bright_yellow, yellow, highscores)
        make_button("Quit", 800, 150, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)


def highscores():
    highscores = True

    while highscores:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Highscores", largeText)
        TextRect.center = ((display_width/5),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)

        make_button("Back to Main", 80, 500, 150, 50, bright_yellow, yellow, start)
        make_button("Quit", 800, 500, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)


def quitgame():
    pygame.quit()
    quit()


def unpaused():
    global pause
    pause = False


def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("Game Paused", largeText)
        TextRect.center = ((display_width/3),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)

        make_button("Resume", 150, 370, 150, 50, bright_green, green, unpaused)
        make_button("Quit", 750, 370, 150, 50, bright_red, red, quitgame)
        
        pygame.display.update()
        clock.tick(15)


def start():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("Castle Defense", largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)

        
        make_button("Start Quest!", 150, 370, 150, 50, bright_green, green, gameloop)
        make_button("Help Menu", 450, 370, 150, 50, bright_yellow, yellow, helpmenu1)
        make_button("Quit", 750, 370, 150, 50, bright_red, red, quitgame)
        make_button("Highscores", 420, 500, 200, 50, bright_blue, blue, highscores)

        pygame.display.update()
        clock.tick(15)
             
start()
pygame.quit()
quit()