class Projectile:

    def __init__(self, type, damage, hit=False):
        """
        type: what type of projectile it is, string
        damage: how much damage it does, int
        """
        self.type = type
        self.damage = damage
        self.hit = hit
        self.exist = True

    def destroy(self):
        if (self.hit):
            self.exist = False

    def is_hit(self, enemy=None):
        if not (type(enemy) == None):
            self.hit = True
            self.deal_damage(enemy)
            self.destroy()
    
    def deal_damage(self, enemy):
        enemy.deal_damage(self.damage)
