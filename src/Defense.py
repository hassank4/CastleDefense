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
