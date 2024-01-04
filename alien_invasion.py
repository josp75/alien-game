import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    app_settings = Settings()
    screen = pygame.display.set_mode((app_settings.screen_width, app_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a skip
    ship = Ship(screen)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events()
        # Redraw the screen during each pass through the loop.
        screen.fill(app_settings.bg_color)
        ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
