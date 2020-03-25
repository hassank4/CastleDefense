import pygame
import time
import random
import os

#--Import Dependencies---------------------------------------
from Assassin import Assassin
from Knight import WeakKnight
from Archer import WeakArcher
from Points import Points
from Wizard import WeakWizard
from Mage import Mage
from Ogre import Ogre
from Menu import Purchase_Menu
from Tower import Tower
from Database import Database
#-------------------------------------------------------------
 
 # Initialize pygame
pygame.font.init()
pygame.init()

defense_names = ["weak_archer1", "weak_knight1", "weak_wizard1"]

WIDTH = 1000
HEIGHT = 600

display_width = 1000
display_height = 600
 
 #--Colours------------------------------------------------------------
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
 #----------------------------------------------------------------------
 

waves = [[5, 0, 0], [0, 5, 0], [0, 0, 5]]

pause = False 
playerName = ''

db = Database()


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Castle Defense')
clock = pygame.time.Clock()
 
 #-- Images--------------------------------------------------------------------------------------
startScreenImg = pygame.image.load('Images/Start-Screen.png')

highscoreMenuImg = pygame.image.load('Images/Highscores-Menu.png')

helpMenu1Img = pygame.image.load('Images/Help-Menu1.png')
helpMenu2Img = pygame.image.load('Images/Help-Menu2.png')
helpMenu3Img = pygame.image.load('Images/Help-Menu3.png')
helpMenu4Img = pygame.image.load('Images/Help-Menu4.png')
helpMenu5Img = pygame.image.load('Images/Help-Menu5.png')

pauseMenuImg = pygame.image.load('Images/Pause-Menu.png')
nameMenuImg = pygame.image.load('Images/Name-Screen.png')


currency_img = pygame.transform.scale(pygame.image.load(os.path.join("images", "crystal_1.png")), (20, 20))
menu_backg = pygame.transform.scale(pygame.image.load(os.path.join("images", "window_1.png")), (400, 110))
buy_archer1 = pygame.transform.scale(pygame.image.load(os.path.join("images/defense/archer1/idle1.png")), (75, 75))

buy_knight1 = pygame.transform.scale(pygame.image.load(os.path.join("images/defense/knight1/idle1.png")), (75, 75))

buy_wizard1 = pygame.transform.scale(pygame.image.load(os.path.join("images/defense/wizard1/idle1.png")), (75, 75))
tower_img = pygame.transform.scale(pygame.image.load(os.path.join("images/main_tower.png")), (200, 200))


# ---------------------------------------------------------------------------------------------------------------------

class Game_map:
    def __init__(self):
        self.game = True #variable to check if game has ended
        self.width = WIDTH
        self.height = HEIGHT
        self.i = 0
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 10
        self.time = time.time()
        self.money = 1000
        self.wave = 0
        self.moving = False
        self.moving_object = None
        self.tower = None
        self.main_tower = Tower(tower_img)
        self.current_wave = waves[self.wave][:]
        self.background = pygame.image.load(os.path.join("images", "temp_background.png"))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.menu = Purchase_Menu(self.width - 200, self.height + 7, menu_backg)
        self.menu.add_btn(buy_archer1, "buy_archer1", 200)
        self.menu.add_btn(buy_knight1, "buy_knight1", 300)
        self.menu.add_btn(buy_wizard1, "buy_wizard1", 400)
        self.points = Points()

    def run(self):
        run = True
        clock = pygame.time.Clock()

        global pause
        

        while run:

            if time.time() - self.time > 1.8:
                self.time = time.time()
                self.enemies.append(random.choice([Mage(0), Assassin(0), Ogre(0)]))
            clock.tick(50)
            # self.create_enemy()

            mouse_pos = pygame.mouse.get_pos()
            # if we are dragging a defense onto the map from the purchase menu
            if self.moving_object:
                # if self.moving_object.place(mouse_pos[0], mouse_pos[1]):  # Check if point is valid for the defense to be placed at
                self.moving_object.move(mouse_pos[0], mouse_pos[1])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.game = False
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                        paused()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if you're moving an object and click
                    #pygame.draw.circle(self.win, (255, 0, 0), mouse_pos, 10, 0)
                    #print(mouse_pos)
                    if self.moving_object:
                        if (self.moving_object.place()):
                            self.towers.append(self.moving_object)

                            self.moving_object.moving = False
                            self.moving_object = None
                    else:
                        # Purchase defense menu clicked
                        purchase_button = self.menu.get_clicked(mouse_pos[0], mouse_pos[1])
                        if purchase_button:
                            price = self.menu.get_item_cost(purchase_button)
                            if self.money >= price:
                                self.money -= price
                                self.add_defense(purchase_button)

                        if self.main_tower.click(mouse_pos[0], mouse_pos[1]):

                            if not self.main_tower.selected:
                                self.main_tower.selected = True
                                self.tower = self.main_tower
                            else:
                                self.main_tower.selected = False

            for tower in self.towers:
                tower.attack(self.enemies, self.points)

            if self.main_tower.get_health() <= 0:
                print("Tower health = 0")
                run = False
                self.game = False

            self.draw()

           

    def create_enemy(self):

        if sum(self.current_wave) == 0:
            if len(self.enemies) == 0:
                self.wave += 1
                self.current_wave = waves[self.wave]
        else:
            #    enemy_groups = [Mage(0), Assassin(0), Ogre(0)]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    #           self.enemies.append(enemy_groups[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    '''
    def check_path_dist(self, tower):
        if '''

    def draw(self):
        self.win.blit(self.background, (0, 0))
        make_button("Surrender", 300, 10, 150, 50, bright_yellow, yellow, highscores)
        make_button("Quit", 500, 10, 150, 50, bright_red, red, quitgame)

        '''
        # display enemies
        for enemy in self.enemies:
            enemy.draw(self.win)
        '''
        for enemy in self.enemies:
            enemy.draw(self.win)
            if enemy.getPosition() == (0, 0):
                del enemy

            # enemy.getPosition()

        # display currency
        text = pygame.font.SysFont("comicsans", 40).render(str(self.money), 1, (0, 0, 0))
        money = pygame.transform.scale(currency_img, (25, 25))

        self.win.blit(text, (5, 1))
        self.win.blit(money, (76, 3))

        # display score
        score_text = pygame.font.SysFont("comicsans", 40).render("Score:", 1, (0, 0, 0))
        score_number = pygame.font.SysFont("comicsans", 40).render(str(self.points.get_points()), 1, (0, 0, 0))
        self.win.blit(score_text, (5, 30))
        self.win.blit(score_number, (5, 55))

        # display kills
        kills_text = pygame.font.SysFont("comicsans", 30).render("Kills", 1, (0, 0, 0))
        assassin_text = pygame.font.SysFont("comicsans", 25).render("Assassin: "+str(self.points.get_kills()[0]), 1, (0, 0, 0))
        mage_text = pygame.font.SysFont("comicsans", 25).render("Mage: "+str(self.points.get_kills()[1]), 1, (0, 0, 0))
        ogre_text = pygame.font.SysFont("comicsans", 25).render("Ogre: "+str(self.points.get_kills()[2]), 1, (0, 0, 0))
        self.win.blit(kills_text, (5, 90))
        self.win.blit(assassin_text, (5, 110))
        self.win.blit(mage_text, (5, 125))
        self.win.blit(ogre_text, (5, 140))

        # draw attack towers
        for tw in self.towers:
            tw.draw(self.win)

        # draw moving defense
        if self.moving_object:
            self.moving_object.draw(self.win)

        # draw menu
        self.menu.draw(self.win)

        # draw main tower
        self.main_tower.draw(self.win)

        pygame.display.update()

    def add_defense(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_archer1", "buy_knight1", "buy_wizard1"]
        object_list = [WeakArcher(self.i, x, y), WeakKnight(self.i, x, y), WeakWizard(self.i, x, y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
            self.i += 1
        except Exception as e:
            print(str(e) + "NOT VALID NAME")

# CREATE GAME MAP INSTANCE
g = Game_map()


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


def gameloop():

    global pause
    global playerName

    gameloop = True
 
    # insert player into the database
    db.insert(playerName, 0)

    playerName = ''

    # print('player name was:' +  playerName)

    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()
       
        g.run()

        pygame.display.update()
        clock.tick(15)

def name():

    name = True
    global playerName

    isLimitExceeded = False

    playerName = ''

    gameDisplay.blit(nameMenuImg, (0, 0))

    while name:
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:                
                keys = pygame.key.name(event.key)

                if(keys.isalpha() or keys.isdigit()):
                    if(keys == 'backspace'):
                        isLimitExceeded = False
                        playerName = playerName[:-1]
                    elif(len(playerName) > 20):
                        isLimitExceeded = True
                    elif(keys == 'space') and (not isLimitExceeded):
                        playerName += ' '
                    elif(not isLimitExceeded):
                        playerName += keys


                    largeText = pygame.font.Font('freesansbold.ttf', 30)
                    
                    TextSurf, TextRect = text_objects(playerName, largeText)
                    TextRect.center = (510, 340)
                    gameDisplay.blit(nameMenuImg, (0, 0))
                    gameDisplay.blit(TextSurf, TextRect)

            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.blit(nameMenuImg, (0, 0))
        if (len(playerName) > 0):
            make_button("Advance", 440, 500, 150, 50, bright_green, green, gameloop)

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


        largeText = pygame.font.Font('freesansbold.ttf', 30)


        scores_lst.sort(key=lambda x: x.get('score'), reverse=True)

        scores_lst = scores_lst[:8]

        for i in range(len(scores_lst)):
            name = scores_lst[i].get("name")
            score = str(scores_lst[i].get("score"))

            x = 370
            y = 150


            TextSurf, TextRect = text_objects(name, largeText)
            TextRect.center = (x, (i * 50) + y)
            gameDisplay.blit(TextSurf, TextRect)

            TextSurf, TextRect = text_objects(score, largeText)
            TextRect.center = (x + 450, (i * 50) + y)
            gameDisplay.blit(TextSurf, TextRect)

        
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
                


        gameDisplay.blit(pauseMenuImg, (0, 0))

        make_button("Resume", 150, 500, 150, 50, bright_green, green, unpaused)
        make_button("Quit", 750, 500, 150, 50, bright_red, red, quitgame)
        
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