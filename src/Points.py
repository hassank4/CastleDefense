from src.Assassin import Assassin
from src.Mage import Mage
from src.Ogre import Ogre


class Points:
    """
    This class is used to keep track of the Points the player accumulates until their tower is destroyed.
    """

    def __init__(self):
        """
        Initializes the point object.
        """
        self.score = 0
        self.assassin_kills = 0
        self.mage_kills = 0
        self.ogre_kills = 0

    def get_points(self):
        """
        Returns the current score accumulated.
        """
        return self.score

    def update_score(self, enemy):
        """
        Changes the number of points and kills depending on which enemy is killed.
        """
        if enemy.getHealth() == 0:
            if type(enemy) == Assassin:
                self.score += 5
                self.assassin_kills += 1
                print(type(enemy))
            elif type(enemy) == Mage:
                self.score += 10
                self.mage_kills += 1
            elif type(enemy) == Ogre:
                self.score += 20
                self.ogre_kills += 1

    def reset(self):
        """
        Sets the score back to 0 for when the users decides to play the game again.
        """
        self.score = 0
        self.assassin_kills = 0
        self.mage_kills = 0
        self.ogre_kills = 0

    def get_kills(self):
        """
        Returns the amount of kills for the three types of enemies.
        """
        return [self.assassin_kills, self.mage_kills, self.ogre_kills]

