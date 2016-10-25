import sys, pygame, math
from constants import settings, colours
from pygame.locals import *

import levels
from levels.Level import Level

sys.path.insert(0, 'shapes/orbs')
sys.path.insert(0, 'shapes/targets')
sys.path.insert(0, 'shapes/obstacles')

from Cursor import Cursor
from Orb import Orb
from Target import Target
from Obstacle import Obstacle

def main():

    # initialize pygame
    pygame.init()

    # open screen
    screen = pygame.display.set_mode(settings.screen_size)

    # load level
    from levels import one # must come after pygame.init()
    level = Level(levels.one.level)

    # play game
    play(screen, level)

    # exit system
    sys.exit()

def play(screen, level):

    score = 0

    # font
    game_Font = pygame.font.SysFont(None, 30)

    # misc variables
    screen_colour = settings.screen_colour
    screen_boundary = pygame.Rect((0, 0), settings.screen_size)

    # game loop
    while True:

        # check for exit code
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return

        # check if cursor is down/up for boost
        screen_colour = colours.BOOST_BLUE if level.check_boost(event.type) else colours.BLACK

        # check if orb hits screen boundary; if so, redirects it elastically
        level.check_boundary(screen_boundary)

        # check if orb is within cursor radius; if so, return it to original position
        level.check_cursor()

        # check if there are any orb interactions
        level.check()

        # update level
        level.update(settings.screen_size)

        # draw background
        screen.fill(screen_colour)

        # update clock
        game_time_ms = pygame.time.get_ticks()
        game_time_s = float(game_time_ms)/1000
        timer = game_Font.render("Time: " + str(game_time_s), True, colours.WHITE)
        screen.blit(timer , (10, 10))

        # update score counter
        score_counter = game_Font.render("Score: " + str(level.score), True, colours.WHITE)
        screen.blit(score_counter , (1100, 10))

        # draw level
        level.draw(screen)

        # update display
        pygame.display.update();

# run main() immediately
if __name__ == '__main__': main()
