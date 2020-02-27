class Projectile:
    """
    Class of the projectile that is shooted by the Defense Object onto an Enemy Object
    """
    
    def __init__(self, type, damage, image, hit=False):
        """
        Creates an instance of the Projectile Class
        type: what type of projectile it is, string
        damage: how much damage it does, int
        """
        self.type = type
        self.damage = damage
        self.hit = hit
        self.exist = True
        self.image = image

    def destroy(self):
        """
        Removes the Projetile from the game
        """
        if (self.hit):
            self.exist = False

    def is_hit(self, enemy=None):
        """
        Decides if the enemy has been hit or not and calls the relevant methods
        """
        if not (type(enemy) == None):
            self.hit = True
            self.deal_damage(enemy)
            self.destroy()
    
    def deal_damage(self, enemy):
        """
        Deals damage to the enemy
        """
        enemy.sub_health(self.damage)

    def get_image(self):
        """
        Get the image associated with the projectile
        """
        return self.image
