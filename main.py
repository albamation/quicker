import sys, pygame, math
from Cursor import Cursor
from Orb import Orb
from Target import Target
from Obstacle import Obstacle

# define game colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BOOST_BLUE = (0, 0, 55)
DEAD_GRAY = (50, 50, 50)
WIN_YELLOW = (255, 255, 0)

def main():

    # initialize pygame
    pygame.init()

    # open screen
    size = width, height = 1200, 400
    screen = pygame.display.set_mode(size)

    # play game
    play(screen, size)

    # exit system
    sys.exit()

def play(screen, size):

    # cursor initialization variables
    cursor_mass_start = 5000
    cursor_rad = 50

    # orb initialization variables
    orb_pos_start = (100, 200)
    orb_rad = 20
    orb_colour = WHITE

    # obstacle initialization variables
    obstacle_rad = 50
    obstacle_pos = (size[0] + obstacle_rad, 200)
    obstacle_vel = (1, 1)

    # target initialization variables
    target_rad = 10
    target_pos = (1100, size[1] + target_rad)
    target_vel = (1, 1)

    # instantiate shapes
    cursor = Cursor(cursor_rad, cursor_mass_start)
    orb = Orb(orb_pos_start, orb_rad, orb_colour, cursor)
    target = Target(target_pos, target_rad, target_vel)
    obstacle = Obstacle(obstacle_pos, obstacle_rad, obstacle_vel)

    # misc variables
    mass_boost = 50000
    screen_color = BLACK

    # define rectangular boundary for orb
    screen_boundary = pygame.Rect((0, 0), size)

    # game loop
    while True:

        # check for exit code
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return

        # check if cursor is down for boost
        if (event.type == pygame.MOUSEBUTTONDOWN) & (orb.cursor.mass == cursor_mass_start):
            orb.cursor.mass = cursor_mass_start + mass_boost
            screen_color = BOOST_BLUE
        if (event.type == pygame.MOUSEBUTTONUP) & (orb.cursor.mass == cursor_mass_start + mass_boost):
            orb.cursor.mass = cursor_mass_start
            screen_color = BLACK

        # check if orb hits screen boundary; if so, redirects it elastically
        if screen_boundary.collidepoint(orb.pos_x, 0) == 0:
            orb.vel_x = -orb.vel_x
        if screen_boundary.collidepoint(0, orb.pos_y) == 0:
            orb.vel_y = -orb.vel_y

        # check if orb is within cursor radius; if so, return it to original position
        if orb.cursor_dist_tot <= orb.cursor.rad:
            orb.pos_x = orb_pos_start[0]
            orb.pos_y = orb_pos_start[1]

        # check if orb is within obstacle radius; if so, game over
        obstacle.check(orb)

        # check if orb is within target radius; if so, get a point
        target.check(orb)

        # update orb (velocity and position)
        orb.update()

        # update obstacle position
        obstacle.update(size)

        # update target position
        target.update(size)

        # draw background
        screen.fill(screen_color)

        # draw shapes
        orb.draw(screen)
        obstacle.draw(screen)
        target.draw(screen)

        # update display
        pygame.display.update();

# run main() immediately
if __name__ == '__main__': main()
