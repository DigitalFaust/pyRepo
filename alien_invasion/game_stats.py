class GameStats():
    """Watching for statistics of game Alien Ivansion"""

    def __init__(self, ai_settings):
        """Initialization of statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Alien invasion starts in active mode
        self.game_active = False

        # Record doesn't have be dropped
        self.high_score = 0

    def reset_stats(self):
        """Initialization of statistics changing due the game"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
