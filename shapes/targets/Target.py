import pygame, math
from constants import colours, physics

# Floating win conditions
class Target:

    pos_x = 0   # initial x position
    pos_y = 0   # initial y position
    vel_x = 0   # initial x velocity
    vel_y = 0   # initial y velocity

    rad = 20    # radius of target

    colour = colours.GREEN

    exists = 1

    # on instantiation
    def __init__(self, pos, rad, vel):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.rad = rad
        self.vel_x = vel[0]
        self.vel_y = vel[1]

    # check if target is touching orb
    def check(self, orb):
        if self.exists:
            dist_x = orb.pos_x - self.pos_x
            dist_y = orb.pos_y - self.pos_y
            dist_tot = math.sqrt(dist_x ** 2 + dist_y ** 2)
            if dist_tot <= self.rad + orb.rad:
                orb.colour = colours.WIN_YELLOW
                self.exists = 0
                return 1
            else:
                return 0

    # update target position
    def update(self, size):

        if self.exists:
            # pac man this bitch
            if self.pos_y < -self.rad:
                self.pos_y = size[1] + self.rad
            if self.pos_x < -self.rad:
                self.pos_x = size[0] + self.rad
                self.pos_y = size[1] + self.rad

            # now shuffle it along
            self.pos_x = self.pos_x - self.vel_x
            self.pos_y = self.pos_y - self.vel_y

    # draw target to screen
    def draw(self, screen):
        if self.exists:
            pygame.draw.circle(screen, self.colour, (self.pos_x, self.pos_y), self.rad, 0)
