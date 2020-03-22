import pygame
import time
import random


import Database

 
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
db = Database()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Castle Defense')
clock = pygame.time.Clock()
 
startScreenImg = pygame.image.load('Images/Start-Screen.png')

highscoreMenuImg = pygame.image.load('Images/Highscores-Menu.png')

helpMenu1Img = pygame.image.load('Images/Help-Menu1.png')
helpMenu2Img = pygame.image.load('Images/Help-Menu2.png')
helpMenu3Img = pygame.image.load('Images/Help-Menu3.png')
helpMenu4Img = pygame.image.load('Images/Help-Menu4.png')
helpMenu5Img = pygame.image.load('Images/Help-Menu5.png')

pause = False 

# --------------------------------------------------------------------------------------------
db = Database()
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

    
        gameDisplay.blit(helpMenu1Img, (0, 0))

        make_button("Next", 10, 520, 100, 50, bright_yellow, yellow, helpmenu2)
        make_button("Quit", 820, 20, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def helpmenu2():
    help = True

    while help:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(helpMenu2Img, (0, 0))

        make_button("Next", 210, 520, 100, 50, bright_yellow, yellow, helpmenu3)
        make_button("Quit", 820, 20, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def helpmenu3():
    help = True

    while help:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(helpMenu3Img, (0, 0))

        make_button("Next", 410, 520, 100, 50, bright_yellow, yellow, helpmenu4)
        make_button("Quit", 820, 20, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def helpmenu4():
    help = True

    while help:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(helpMenu4Img, (0, 0))

        make_button("Next", 610, 520, 100, 50, bright_yellow, yellow, helpmenu5)
        make_button("Quit", 820, 20, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def helpmenu5():
    help = True

    while help:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(helpMenu5Img, (0, 0))

        make_button("Main", 810, 520, 100, 50, bright_yellow, yellow, start)
        make_button("Quit", 820, 20, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)


def easygameloop():
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
        TextSurf, TextRect = text_objects("Easy Game Map", largeText)
        TextRect.center = ((display_width/4),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)

        
        make_button("Game End", 800, 400, 150, 50, bright_yellow, yellow, highscores)
        make_button("Quit", 800, 500, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def mediumgameloop():
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
        TextSurf, TextRect = text_objects("Medium Game Map", largeText)
        TextRect.center = ((display_width/4),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)

        
        make_button("Game End", 800, 400, 150, 50, bright_yellow, yellow, highscores)
        make_button("Quit", 800, 500, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def hardgameloop():
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
        TextSurf, TextRect = text_objects("Hard Game Map", largeText)
        TextRect.center = ((display_width/4),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)

        
        make_button("Game End", 800, 400, 150, 50, bright_yellow, yellow, highscores)
        make_button("Quit", 800, 500, 150, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def difficulty():
    diff = True

    while diff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Difficulty", largeText)
        TextRect.center = ((display_width/6),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)

        make_button("Easy", 100, 300, 200, 100, bright_green, green, easygameloop)
        make_button("Medium", 400, 300, 200, 100, bright_yellow, yellow, mediumgameloop)
        make_button("Hard", 700, 300, 200, 100, bright_red, red, hardgameloop)

        pygame.display.update()
        clock.tick(15)

def name():

    name = True
    userName = []

    while name:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:                
                keys = pygame.key.name(event.key)

                if(keys.isalpha or keys.isdigit):
                    userName.append(keys)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        final = ''

        for s in userName:
            final += s

        print(final)


        make_button("Advance", 100, 500, 150, 50, bright_green, green, difficulty)

        pygame.display.update()
        clock.tick(15)



def highscores():
    highscores = True

    while highscores:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(highscoreMenuImg, (0, 0))

        # Getting a list of all high scores from the database
        scores_lst = db.get_all_docs()

        make_button("Back to Main", 40, 20, 150, 50, bright_yellow, yellow, start)
        make_button("Quit", 830, 20, 150, 50, bright_red, red, quitgame)

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
                
        gameDisplay.blit(startScreenImg, (0, 0))

        make_button("Start Quest!", 150, 370, 150, 50, bright_green, green, name)
        make_button("Help Menu", 450, 370, 150, 50, bright_yellow, yellow, helpmenu1)
        make_button("Quit", 750, 370, 150, 50, bright_red, red, quitgame)
        make_button("Highscores", 420, 500, 200, 50, bright_blue, blue, highscores)

        pygame.display.update()
        clock.tick(15)
             
start()
pygame.quit()
quit()