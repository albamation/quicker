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
    from levels import four # must come after pygame.init()
    level = Level(levels.four.level)

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

    display_start_text = 1
    time_delay_offset = 0

    # game loop
    while True:

        # check for exit code
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            if display_start_text == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for orb in level.orbs:
                        orb.in_play = 1
                        display_start_text = 0
                        time_delay_offset = pygame.time.get_ticks()

        level.level_check()

        # check if cursor is down/up for boost
        if level.level_complete == 0:
            screen_colour = colours.BOOST_BLUE if level.check_boost(event.type) else colours.BLACK

        # check if orb hits screen boundary; if so, redirects it elastically
        if level.level_complete == 0:
            level.check_boundary(screen_boundary)

        # check if orb is within cursor radius; if so, return it to original position
        if level.level_complete == 0:
            level.check_cursor()

        # check if there are any orb interactions
        if level.level_complete == 0:
            level.check()

        # update level
        if level.level_complete == 0:
            level.update(settings.screen_size)

        # draw background
        if level.level_complete == 0:
            screen.fill(screen_colour)

        # update clock
        if level.level_complete == 0:
            game_time_ms = pygame.time.get_ticks() - time_delay_offset
            game_time_s = float(game_time_ms)/1000
            if display_start_text == 1:
                game_time_s = 0
            timer = game_Font.render("Time: " + str(game_time_s), True, colours.WHITE)
            screen.blit(timer , (10, 10))

        # update point counter
        if level.level_complete == 0:
            point_counter = game_Font.render("Points: " + str(level.points), True, colours.WHITE)
            screen.blit(point_counter , (10, 30))

        # draw level
        if level.level_complete == 0:
            level.draw(screen)

        # Check if level is complete
        if level.level_complete:
            level_over_text = game_Font.render("Level Complete!" , True, colours.WHITE)
            level_points_text = game_Font.render("Points Collected: " + str(level.points) , True, colours.WHITE)
            game_time_final = game_time_s
            level_time_text = game_Font.render("Total Time: " + str(game_time_final), True, colours.WHITE)
            time_bonus = (60 - game_time_s)/5
            if time_bonus < 0:
                time_bonus = 0
            final_score = level.points + time_bonus # this needs tinkering
            level_final_score_text = game_Font.render("Final Score: " + str(final_score), True, colours.WHITE)
            screen.blit(level_over_text , (500, 200))
            screen.blit(level_points_text , (500, 300))
            screen.blit(level_time_text , (500, 400))
            screen.blit(level_final_score_text , (500, 500))
            pygame.display.update();

        # update display
        if level.level_complete == 0:
            if display_start_text == 1:
                click_to_start_text = game_Font.render("Click Anywhere To Begin" , True, colours.WHITE)
                screen.blit(click_to_start_text , (500, 200))
            pygame.display.update();

# run main() immediately
if __name__ == '__main__': main()
