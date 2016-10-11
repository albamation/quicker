import sys, pygame
import math

# define game colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():

    # initialize pygame
    pygame.init()

    # open screen
    size = width, height = 1200, 400
    screen = pygame.display.set_mode(size)

    # play game
    play(screen)

    # exit system
    sys.exit()

def play(screen):

    # define game variables
    orb_pos = (100, 200)
    orb_rad = 20
    orb_vel_x = 0 #initial x velocity
    orb_vel_y = 0 #initial y velocity
    cursor_mass = 200
    gravity_constant = 1
    time_constant = 1 #this accounts for the amount of time between updates (equivalent to fps value)

    # game loop
    while True:

        # check for exit code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # render black background
        screen.fill(BLACK)

        # get mouse postition
        mouse_pos = pygame.mouse.get_pos()

        # calculate distance between cursor and circle
        separation_dist_x = mouse_pos[0]-orb_pos[0]
        separation_dist_y = mouse_pos[1]-orb_pos[1]
        separation_dist_tot = math.sqrt(separation_dist_x**2 + separation_dist_y**2)

        # calculate acceleration
        acceleration_tot = gravity_constant*cursor_mass/(separation_dist_tot**2)
        acceleration_x = (separation_dist_x/separation_dist_tot)*acceleration_tot
        acceleration_y = (separation_dist_y/separation_dist_tot)*acceleration_tot

        # calculate velocity
        orb_vel_x = orb_vel_x + acceleration_x/time_constant
        orb_vel_y = orb_vel_y + acceleration_y/time_constant

        # update orb position
        orb_pos = (int(orb_pos[0] + orb_vel_x/time_constant), int(orb_pos[1] + orb_vel_y/time_constant))


        # draw target orb
        pygame.draw.circle(screen, WHITE, orb_pos, orb_rad, 0)

        # update display
        pygame.display.update();

if __name__ == '__main__': main()
