import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class presents single alien"""

    def __init__(self, ai_settings, screen):
        """Initializes alien and sets his initial position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading image of alien and setting attributes 'rect'
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.rect = self.image.get_rect()

        # Every new alien appears in the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Saving exact position of alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Output alien in the current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Moves alien to the right"""
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x

    def check_edges(self):
        """Returns True if aliens is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Moves alien to the left or to the right"""
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.rect.x = self.x
