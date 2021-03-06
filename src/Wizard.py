from Defense import Defense
from Projectile import Projectile

WIZARDATTACK = ["Images/Defense/wizard1/attack1.png", "Images/Defense/wizard1/attack2.png", "Images/Defense/wizard1/attack3.png", "Images/Defense/wizard1/attack4.png", "Images/Defense/wizard1/attack5.png"]
WIZARDIDLE = ["Images/Defense/wizard1/idle1.png", "Images/Defense/wizard1/idle2.png", "Images/Defense/wizard1/idle3.png", "Images/Defense/wizard1/idle4.png", "Images/Defense/wizard1/idle5.png"]
class WeakWizard(Defense):

    def __init__(self, wizard_id, x_coord, y_coord):
        super().__init__(wizard_id, 60, 1, x_coord, y_coord, WIZARDIDLE#"Images/Defense/wizard1/idle1.png"
                         , WIZARDATTACK)#"Images/Defense/wizard1/attack5.png")
        self.projectile = Projectile("magic", super().get_attack_damage(), "Images/Projectile/wizard/level1_ball1.png")

    def get_projectile(self):
        return self.projectile


class IntermediateWizard(Defense):

    def __init__(self, wizard_id, x_coord, y_coord):
        super().__init__(wizard_id, 80, 2, x_coord, y_coord, "Images/Defense/wizard2/idle1.png"
                         , "Images/Defense/wizard2/attack5.png")
        self.projectile = Projectile("magic", super().get_attack_damage(), "Images/Projectile/wizard/level2_ball1.png")

    def get_projectile(self):
        return self.projectile


class StrongWizard(Defense):

    def __init__(self, wizard_id, x_coord, y_coord):
        super().__init__(wizard_id, 100, 3, x_coord, y_coord, "Images/Defense/wizard3/idle1.png"
                         , "Images/Defense/wizard3/attack5.png")
        self.projectile = Projectile("magic", super().get_attack_damage(), "Images/Projectile/wizard/level3_ball1.png")

    def get_projectile(self):
        return self.projectile

