from Defense import Defense
from Projectile import Projectile
import pygame

ARCHERATTACK = ["Images/Defense/archer1/attack1.png", "Images/Defense/archer1/attack2.png", "Images/Defense/archer1/attack3.png", "Images/Defense/archer1/attack4.png", "Images/Defense/archer1/attack5.png"]
ARCHERIDLE = ["Images/Defense/archer1/idle1.png", "Images/Defense/archer1/idle2.png", "Images/Defense/archer1/idle3.png", "Images/Defense/archer1/idle4.png", "Images/Defense/archer1/idle5.png"]
class WeakArcher(Defense):

    def __init__(self, archer_id, x_coord, y_coord):
        super().__init__(archer_id, 15, 1, x_coord, y_coord, ARCHERIDLE#"Images/Defense/archer1/idle1.png"
                         , ARCHERATTACK)#"Images/Defense/archer1/attack2.png")
        self.projectile = Projectile("arrow", super().get_attack_damage(), "Images/Projectile/archer/basic_arrow1.png")

    def get_projectile(self):
        return self.projectile


class IntermediateArcher(Defense):

    def __init__(self, archer_id, x_coord, y_coord):
        super().__init__(archer_id, 20, 2, x_coord, y_coord, "Images/Defense/archer2/idle1.png"
                         , "Images/Defense/archer2/attack2.png")
        self.projectile = Projectile("arrow", super().get_attack_damage(),
                                     "Images/Projectile/archer/blue_fire_arrow1.png")

    def get_projectile(self):
        return self.projectile


class StrongArcher(Defense):

    def __init__(self, archer_id, x_coord, y_coord):
        super().__init__(archer_id, 25, 3, x_coord, y_coord, "Images/Defense/archer3/idle1.png"
                         , "Images/Defense/archer3/attack2.png")
        self.projectile = Projectile("arrow", super().get_attack_damage(), "Images/Projectile/archer/fire_arrow1.png")

    def get_projectile(self):
        return self.projectile
