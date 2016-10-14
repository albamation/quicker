import sys, pygame
import math

# define game colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BOOST_BLUE = (0, 0, 55)

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

    # define game variables
    orb_pos = (100, 200)
    orb_rad = 20
    orb_mass = 1
    orb_vel_x = 0 #initial x velocity
    orb_vel_y = 0 #initial y velocity
    initial_cursor_mass = 5000
    cursor_mass = initial_cursor_mass
    cursor_rad = 50
    gravity_constant = 1
    friction_constant = 0.005
    time_constant = 1 #this accounts for the amount of time between frames (equivalent to fps value)
    obstacle_rad = 50
    obstacle_pos = (size[0] + obstacle_rad, 200)
    obstacle_vel = 1
    mass_boost = 50000
    screen_color = BLACK

    # define rectangular boundary for orb
    screen_boundary = pygame.Rect((0, 0), size)

    # game loop
    while True:

        # check for exit code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # render black background
        screen.fill(screen_color)

        # get mouse postition
        mouse_pos = pygame.mouse.get_pos()

        # check if cursor is down for boost
        if (event.type == pygame.MOUSEBUTTONDOWN) & (cursor_mass == initial_cursor_mass):
            cursor_mass = initial_cursor_mass + mass_boost
            screen_color = BOOST_BLUE
        if (event.type == pygame.MOUSEBUTTONUP) & (cursor_mass == initial_cursor_mass + mass_boost):
            cursor_mass = initial_cursor_mass
            screen_color = BLACK

        # check if orb hits screen boundary, redirects it elastically if it does
        if screen_boundary.collidepoint(orb_pos[0],0)==0:
            orb_vel_x = -orb_vel_x
        if screen_boundary.collidepoint(0,orb_pos[1])==0:
            orb_vel_y = -orb_vel_y

        # check if orb is within cursor radius; if so, return it to original position
        cursor_pos_x_plus = mouse_pos[0] + cursor_rad
        cursor_pos_x_minus = mouse_pos[0] - cursor_rad
        cursor_pos_y_plus = mouse_pos[1] + cursor_rad
        cursor_pos_y_minus = mouse_pos[1] - cursor_rad
        if (orb_pos[0] <= cursor_pos_x_plus) & (orb_pos[0] >= cursor_pos_x_minus):
            if (orb_pos[1] <= cursor_pos_y_plus) & (orb_pos[1] >= cursor_pos_y_minus):
                # orb is within cursor boundary
                orb_pos = (100, 200)


        # calculate distance between cursor and orb
        separation_dist_x = mouse_pos[0]-orb_pos[0]
        separation_dist_y = mouse_pos[1]-orb_pos[1]
        separation_dist_tot = math.sqrt(separation_dist_x**2 + separation_dist_y**2)

        # calculate gravity force
        force_gravity_x = separation_dist_x*gravity_constant*cursor_mass*orb_mass/(separation_dist_tot**3)
        force_gravity_y = separation_dist_y*gravity_constant*cursor_mass*orb_mass/(separation_dist_tot**3)

        # calculate friction force
        force_friction_x = -friction_constant*orb_vel_x*abs(orb_vel_x)
        force_friction_y = -friction_constant*orb_vel_y*abs(orb_vel_y)

        # calculate net force
        force_net_x = force_gravity_x + force_friction_x
        force_net_y = force_gravity_y + force_friction_y

        # calculate acceleration
        acceleration_x = force_net_x/orb_mass
        acceleration_y = force_net_y/orb_mass

        # calculate velocity
        orb_vel_x = orb_vel_x + acceleration_x/time_constant
        orb_vel_y = orb_vel_y + acceleration_y/time_constant

        # update orb position
        orb_pos = (int(orb_pos[0] + orb_vel_x/time_constant), int(orb_pos[1] + orb_vel_y/time_constant))

        # draw target orb
        pygame.draw.circle(screen, WHITE, orb_pos, orb_rad, 0)

        # update obstacle position
        if obstacle_pos[0] < -obstacle_rad:
            obstacle_pos = (size[0] + obstacle_rad, 200)

        obstacle_pos = (obstacle_pos[0]- obstacle_vel, obstacle_pos[1])

        # draw obstacle
        pygame.draw.circle(screen, RED, obstacle_pos, obstacle_rad, 0)

        # update display
        pygame.display.update();

if __name__ == '__main__': main()
