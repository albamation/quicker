import sys, pygame

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

    # game loop
    while True:

        # check for exit code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # render black background
        screen.fill(BLACK)

        # get mouse postition

        # calculate velocity

        # update orb position

        # draw target orb
        pygame.draw.circle(screen, WHITE, orb_pos, orb_rad, 0)

        # update display
        pygame.display.update();

if __name__ == '__main__': main()
