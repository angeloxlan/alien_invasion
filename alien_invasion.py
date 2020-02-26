import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Initialize game and create a screen object."""

    pygame.init()

    # Instance of Settings
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings=ai_settings, screen=screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        # Call check_events method to watch for keyboard and mouse events.
        gf.check_events(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets)

run_game()