import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for manage bullets shooted by ship"""

    def __init__(self, ai_settings, screen, ship):
        """Creates bullet's object in current ship's position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Creation bullet in position (0, 0) and setting correct position

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Bullet's position contains as a float format 

        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves bullet from bottom to top on the screen"""

        # Updates position of bullet in floating format

        self.y -= self.speed_factor

        # Updates position of rectangle

        self.rect.y = self.y

    def draw_bullet(self):
        """Output bullet of the screen"""

        pygame.draw.rect(self.screen, self.color, self.rect)
