import pygame, math
from constants import colours, physics

# The player character orb
class Orb:

    pos_start = (0, 0)

    pos_x = 0   # initial x position
    pos_y = 0   # initial y position
    vel_x = 0   # initial x velocity
    vel_y = 0   # initial y velocity

    rad = 20    # radius of orb
    mass = 1    # weight of orb

    colour = colours.WHITE

    cursor = False
    cursor_dist_x = 0
    cursor_dist_y = 0
    cursor_dist_tot = 0

    # on instantiation
    def __init__(self, pos, rad, colour, cursor):

        # remember starting positions\
        self.pos_start = pos

        # set variables
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.rad = rad
        self.colour = colour
        self.cursor = cursor

        # get initial cursor position
        self.get_cursor()

    # get distances between orb and cursor
    def get_cursor(self):

        # get mouse postition
        mouse_pos = pygame.mouse.get_pos()

        # calculate distance between cursor and orb
        self.cursor_dist_x = mouse_pos[0] - self.pos_x
        self.cursor_dist_y = mouse_pos[1] - self.pos_y
        self.cursor_dist_tot = math.sqrt(self.cursor_dist_x ** 2 + self.cursor_dist_y ** 2)

    # update orb position and velocity based on cursor and physics
    def update(self):

        # update cursor position
        self.get_cursor()

        # calculate gravity force
        force_gravity_x = self.cursor_dist_x * physics.gravity * self.cursor.mass * self.mass / (self.cursor_dist_tot ** 3)
        force_gravity_y = self.cursor_dist_y * physics.gravity * self.cursor.mass * self.mass / (self.cursor_dist_tot ** 3)

        # calculate friction force
        force_friction_x = -physics.friction * self.vel_x * abs(self.vel_x)
        force_friction_y = -physics.friction * self.vel_y * abs(self.vel_y)

        # calculate net force
        force_net_x = force_gravity_x + force_friction_x
        force_net_y = force_gravity_y + force_friction_y

        # calculate acceleration
        acceleration_x = force_net_x / self.mass
        acceleration_y = force_net_y / self.mass

        # update velocity
        self.vel_x = self.vel_x + acceleration_x / physics.time
        self.vel_y = self.vel_y + acceleration_y / physics.time

        # update position
        self.pos_x = int((self.pos_x + self.vel_x) / physics.time)
        self.pos_y = int((self.pos_y + self.vel_y) / physics.time)

    # draw orb to screen
    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.pos_x, self.pos_y), self.rad, 0)
        pygame.draw.circle(screen, self.colour, (self.pos_start[0], self.pos_start[1]), self.rad, 1)
