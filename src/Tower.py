class Tower:
    """
    The class for a Tower. Takes a path for the graphic and starts the Tower off with 100 health.
    """
    def __init__(self, img_path):
        """Initialize a Tower."""
        self.health = 100
        self.img_path = img_path

    def __str__(self):
        """Return a string representation of Tower's health."""
        return "Health: " + str(self.health)

    def get_health(self):
        """Return Tower's HP."""
        return self.health

    def take_damage(self, amount):
        """Take a damage amount and deduct it from the Tower's health."""
        # Ensure Tower's health is non-negative.
        if self.health > amount:
            self.health -= amount
        else:
            self.health = 0