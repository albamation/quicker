import pygame, math
from constants import colours, physics

# The BIG BAD
class Obstacle:

    pos_x = 0   # initial x position
    pos_y = 0   # initial y position
    vel_x = 0   # initial x velocity
    vel_y = 0   # initial y velocity

    rad = 20    # radius of obstacle
    orbit_rad = 100 # in case of circular motion

    orbit_center = (0 , 0)
    theta = 0

    colour = colours.RED

    exists = 1

    #Define certain trajectories
    #Legend:
    # rtl - Linear (right to left)
    # ltr - Linear (left to right)
    # cw - Circular (CW)
    # ccw - Circular (CCW)
    motion = "rtl"

    # on instantiation
    def __init__(self, pos, rad, vel, motion, orbit_rad):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.rad = rad
        self.vel_x = vel[0]
        self.vel_y = vel[1]
        self.motion = motion
        self.orbit_rad = orbit_rad
        self.orbit_center = (self.pos_x , self.pos_y + self.orbit_rad)

    # check if obstacle is touching orb
    def check(self, orb):
        if self.exists:
            dist_x = orb.pos_x - self.pos_x
            dist_y = orb.pos_y - self.pos_y
            dist_tot = math.sqrt(dist_x ** 2 + dist_y ** 2)
            if dist_tot <= self.rad + orb.rad:
                orb.colour = colours.DEAD_GRAY
                self.exists = 0
                return 1
            else:
                return 0

    # update obstacle position
    def update(self, size):
        if self.exists:
            if self.motion == "rtl":
                if self.pos_x < -self.rad:
                    self.pos_x = size[0] + self.rad
                self.pos_x = self.pos_x - self.vel_x
            elif self.motion == "ltr":
                if self.pos_x > self.rad + size[0]:
                    self.pos_x = -self.rad
                self.pos_x = self.pos_x + self.vel_x
            elif self.motion == "cw":
                self.theta = self.theta + self.vel_x/(10*6.28)
                self.pos_x = self.orbit_center[0] + int(self.orbit_rad*math.cos(self.theta))
                self.pos_y = self.orbit_center[1] + int(self.orbit_rad*math.sin(self.theta))
            elif self.motion == "ccw":
                self.theta = self.theta - self.vel_x/(10*6.28)
                self.pos_x = self.orbit_center[0] + int(self.orbit_rad*math.cos(self.theta))
                self.pos_y = self.orbit_center[1] + int(self.orbit_rad*math.sin(self.theta))


    # draw obstacle to screen
    def draw(self, screen):
        if self.exists:
            pygame.draw.circle(screen, self.colour, (self.pos_x, self.pos_y), self.rad, 0)
