import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialization of space ship and setting it starts position"""
        super(Ship, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # Loading space ship image and getting rectangle
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        #Every new ship appears about bottom's screen edge
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Saving float coordinates about bottom edge of screen
        self.center = float(self.rect.centerx)

        # Flag of motion
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship's position according with flag"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Updating attributes rect based on self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Drawning ship in the current position"""

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Places ship in the center of bottom side"""
        self.center = self.screen_rect.centerx
