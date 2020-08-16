class Settings():
    """Class containing all settings of the game Alien Invasion"""

    def __init__(self):
        """Initialization of game settings"""
        # Screen parameters
        self.screen_width = 1366
        self.screen_height = 700
        self.bg_color = (20, 110, 200)

        # Bullet's paremeters
        self.bullet_speed_factor = 3
        self.bullet_width = 1400
        self.bullet_height = 7
        self.bullet_color = (160, 125, 140)
        self.bullets_allowed = 3

        # Alien's settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 means motion to the right and -1 to the left
        self.fleet_direction = 1

        # Ship's paramters
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Pace of boosting the game
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # Pace of increasing cost of alien
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializes settings changing during the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50

        # fleet_direction = 1 means motion to the right and -1 to the left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increasing settings of speed"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
    
    def prep_score(self):
        """Transform current score into graphical view"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounde_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
