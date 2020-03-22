import os

import pygame
import math
import time


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

    def place(self, x, y):
        """
        Makes sure that the defense object is able to be placed down at the current coordinates and then
        calls set_coordinates to place the defense object down.
        """
        # R: 141
        # G: 126
        # B: 123

        line_one = [(233, 595, [0, 1]),
                    (233, 568, [0, 1, 2]),
                    (180, 534, [1, 2, 3]),
                    (80, 493, [2, 3, 4, 5]),
                    (40, 416, [3, 4, 5]),
                    (76, 304, [4, 5, 6]),
                    (216, 250, [5, 6, 7]),
                    (289, 92, [6, 7, 8]),
                    (356, 66, [7, 8]),
                    (557, 75, [8, 9]),
                    (651, 183, [8, 9, 10]),
                    (664, 386, [9, 10, 11]),
                    (1063, 400, [11, 12])]  # len = 13

        line_two = [(318, 598),
                    (317, 551),
                    (268, 478),
                    (154, 440),
                    (132, 394),
                    (156, 355),
                    (292, 293),
                    (327, 172),
                    (546, 162),
                    (562, 387),
                    (648, 482),
                    (874, 490),
                    (1064, 483)]  # len = 13

        for i in range(len(line_one)):
            c_x = line_one[i][0]
            c_y = line_one[i][1]
            points = line_one[i][2]

            if (i == 0):
                if ((x >= c_x and x <= line_one[i + 1][0]) or (y >= c_y and y <= line_one[i + 1][1])):
                    print("can't place here")
                    return False
            else:
                if ((x >= c_x and x <= line_one[i + 1][0]) or (y >= c_y and y <= line_one[i + 1][1])):
                    print("can't place here")
                    return False
                elif ((x <= c_x and x >= line_one[i - 1][0]) or (y <= c_y and y >= line_one[i - 1][1])):
                    print("can't place here")
                    return False

            for j in points:
                if ((x >= c_x and x <= line_two[j][0]) or (y >= c_y and y <= line_two[j][1])):
                    print("can't place here")
                    return False
        self.set_coordinates(x, y)
        return True

    def move(self, x, y):
        """
        Move object to given x and y
        """
        self.x = x
        self.y = y

    def draw(self, win):
        defense = pygame.transform.scale(pygame.image.load(os.path.join(self.get_idle_image())), (75, 75))
        win.blit(defense, (self.x - defense.get_width() // 2, self.y - defense.get_height() // 2))

    def attack(self, enemies):
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

            # if first_enemy.x < self.x:

