import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

import game_functions as gf

def run_game():
    
    # Initialization pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Creation of a ship, a group of bullets and aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    #Creation aliens's fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Creation samples of GameStats and Scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    pygame.display.set_caption("Alien Invasion")
    # Creation of button Play
    play_button = Button(ai_settings, screen, "Play")

    # Runing main cycle
    while True:
        # Watching events events of keyboard and mouse
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
