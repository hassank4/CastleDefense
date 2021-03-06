import os

import pygame
import math
import time

PATH = [(256, 592), (242, 536), (155, 489), (90, 434), (86, 367), (117, 320), (202, 295), (249, 224), (271, 141), (335, 119), (413, 111), (499, 113), (544, 140), (563, 209), (567, 266), (567, 350), (587, 419), (651, 445), (711, 447), (776, 447), (837, 448), (880, 445), (947, 442), (993, 443)]
class Defense:
    """
    This is the Defense Class that contains the essentials of a defense character in the game.
    """

    def __init__(self, id, attack_damage, level, x_coord, y_coord, idle_image, attack_image):
        """
        This initializes a defense object.
        """
        self.id = id
        self.attack_damage = attack_damage
        self.level = level
        self.x = x_coord
        self.y = y_coord
        self.idle_image = idle_image
        self.attack_image = attack_image
        self.moving = False
        self.range = 200
        self.inRange = False
        self.timer = time.time()
        self.pictureCount = 0

    def set_range(self, new_range):
        self.range = new_range

    def get_id(self):
        """
        Return the id associated with the defense character.
        """
        return self.id

    def get_attack_damage(self):
        """
        Return the attack damage the defense character is able to do.
        """
        return self.attack_damage

    def set_attack_damage(self, attack_damage: int):
        """
        Changes the attack damage of the defense character.
        :param attack_damage: The attack damage amount that is used by the character
        """
        self.attack_damage = attack_damage

    def if_max_level(self) -> bool:
        """
        Return whether the defense character is at max level or not.
        """
        return self.level == 3

    def set_level(self, level: int):
        """
        Sets the level of the defense character
        :param level: The level of the character
        """
        self.level = level

    def get_coordinates(self):
        """
        Returns the x and y coordinates of the defense character on the map.
        """
        return self.x, self.y

    def set_coordinates(self, x_coord: int, y_coord: int):
        """
        Sets the x and y coordinates of the defense character.
        """
        self.x = x_coord
        self.y = y_coord

    def get_idle_image(self):
        """
        Get the image associated with the character when idled
        """
        return self.idle_image

    def get_attack_image(self):
        """
        Get the image associated with the character when attacking
        """
        return self.attack_image

    def findClosestPoints(self, x, y):
        points = []
        for point in PATH:
            dis = math.sqrt((x - point[0])**2 + (y - point[1])**2)
            points.append([dis, point])
        points.sort(key=lambda x: x[0])

        return points[0][1], points[1][1]


    def place(self):
        """
        Makes sure that the defense object is able to be placed down at the current coordinates and then
        calls set_coordinates to place the defense object down.
        """
        # R: 141
        # G: 126
        # B: 123
        x, y = self.x, self.y
        width = 55
        p1, p2 = self.findClosestPoints(x, y)
        m = findSlope(p1, p2)
        if m == 0:
            slope = 100000000000000000
        else:
            slope = -(1/m)
        b = (slope * x) * -1 + y
        line = lineFromPoints(p1, p2)
        point = findIntersection(line, [slope, b])
        
        distance = math.sqrt((x - point[0])**2 + (y - point[1])**2)
       # print(distance)
        if distance <= width:
            return False

        #self.set_coordinates(x, y)
        return True

    def move(self, x, y):
        """
        Move object to given x and y
        """
        self.x = x
        self.y = y

    def draw(self, surface):

        if not self.moving:
            self.pictureCount += 1
            if self.pictureCount >= len(self.attack_image) * 6:
                self.pictureCount = 0

            if self.inRange:
                pictures = self.get_attack_image()
                picture = pictures[self.pictureCount//6]
            else:
                pictures = self.get_idle_image()
                picture = pictures[self.pictureCount//6]
        else:
            self.pictureCount = 0
            pictures = self.get_idle_image()
            picture = pictures[self.pictureCount//6]
            
        defense = pygame.transform.scale(pygame.image.load(os.path.join(picture)), (75, 75))
        surface.blit(defense, ((self.x - defense.get_width() // 2), (self.y - defense.get_height() // 2)))

    def attack(self, enemies, points):
        self.inRange = False
        closest_enemies = []
        for enemy in enemies:
            enemy_x, enemy_y = enemy.x, enemy.y
            distance = math.sqrt((self.x - enemy_x)**2 + (self.y - enemy_y)**2)

            if distance < self.range:
                self.inRange = True
                closest_enemies.append(enemy)

        closest_enemies.sort(key=lambda x: x.x)
        if len(closest_enemies) > 0:
            first_enemy = closest_enemies[0]
            
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                if first_enemy.subHealth(self.attack_damage):
                    enemies.remove(first_enemy)
                    points.update_score(first_enemy)

            # if first_enemy.x < self.x:

def lineFromPoints(point1, point2): 

    m = findSlope(point1, point2)
    b = (m * point1[0]) * -1 + point1[1]
    return [m, b]
    # a = point2[1] - point1[1] 
    # b = point1[0] - point2[0]  
    # c = a*(point1[0]) + b*(point2[1])

    # return [a,b,c]

def findSlope(point1, point2):
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    if dx == 0:
        dx += 0.000000000001
    m = dy / dx
    return m


def findIntersection(line1, line2):
    m = line1[0] - line2[0]
    b = line2[1] - line1[1]
    x = b / m
    y = line1[0] * x + line1[1]
    return [x, y]
