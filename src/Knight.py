from Defense import Defense
from Projectile import Projectile


class WeakKnight(Defense):

    def __init__(self, knight_id, x_coord, y_coord):
        super().__init__(knight_id, 35, 1, x_coord, y_coord, "Images/Defense/knight1/idle1.png"
                         , "Images/Defense/knight1/attack2.png")
        self.projectile = Projectile("spear", super().get_attack_damage(), "Images/Projectile/knight/basic_spear1.png")

    def get_projectile(self):
        return self.projectile


class IntermediateKnight(Defense):

    def __init__(self, knight_id, x_coord, y_coord):
        super().__init__(knight_id, 40, 2, x_coord, y_coord, "Images/Defense/knight2/idle1.png"
                         , "Images/Defense/knight2/attack2.png")
        self.projectile = Projectile("spear", super().get_attack_damage(), "Images/Projectile/knight/level2_spear1.png")

    def get_projectile(self):
        return self.projectile


class StrongKnight(Defense):

    def __init__(self, knight_id, x_coord, y_coord):
        super().__init__(knight_id, 50, 3, x_coord, y_coord, "Images/Defense/knight3/idle1.png"
                         , "Images/Defense/knight3/attack2.png")
        self.projectile = Projectile("spear", super().get_attack_damage(), "Images/Projectile/knight/level3_spear1.png")

    def get_projectile(self):
        return self.projectile
