class Defense:
    """
    This is the Defense Class that contains the essentials of a defense character in the game.
    """

    def __init__(self, id, health, attack_damage, level, x_coord, y_coord, image):
        """
        This initializes a defense object.
        """
        self.id = id
        self.health = health
        self.attack_damage = attack_damage
        self.level = level
        self.x = x_coord
        self.y = y_coord
        self.image = image

    def get_id(self):
        """
        Return the id associated with the defense character.
        """
        return self.id

    def get_health(self) -> int:
        """
        Return the health of the defense character.
        """
        return self.health

    def update_health(self, attack:int):
        """
        Updates the health of the defense character based on how much it was attacked.
        :param attack: The attack damage done by the enemy
        """
        if (self.health - attack) < 0:
            self.health = 0
        else:
            self.health = self.health - attack

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
        if self.level == 3:
            return True
        else:
            return False

    def set_level(self, level: int) -> int:
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

    def if_dead(self) -> bool:
        """
        Returns whether the defense character is dead and can no longer fight the enemies.
        """
        if self.health == 0:
            return True
        else:
            return False

    


