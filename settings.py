class Settings:
    """A class to store all setting  for Alien Invasion"""
    def __init__(self):
        """Initialize the game's setting."""
        # screen setting
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0,0,255)

        # ship setting
        self.ship_speed = 1.5
        # Bullet setting
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Alien setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        #fleet_directions of represents rights; -1 represents left.
        self.fleet_directions = 1
