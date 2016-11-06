import sys,pygame, math
from constants import colours, physics
from sounds import sounds

# Floating win conditions
class Target:

    pos_x = 0   # initial x position
    pos_y = 0   # initial y position
    vel_x = 0   # initial x velocity
    vel_y = 0   # initial y velocity
    vel_circ = 2*math.pi/60 # initial circular velocity

    rad = 20    # radius of target
    orbit_rad = 0 # in case of circular motion
    orbit_center = (0, 0)
    theta = 0

    colour = colours.GREEN

    exists = 1

    # on instantiation
    def __init__(self, pos, rad, vel):
        self.theta = -2*math.pi*pos[2]/360
        self.pos_x = pos[0] + rad[1]*math.cos(self.theta)
        self.pos_y = pos[1] + rad[1]*math.sin(self.theta)
        self.rad = rad[0]
        self.vel_x = vel[0]
        self.vel_y = vel[1]
        self.vel_circ = vel[2]*math.pi/360 # vel[2] refers to number of degrees to rotate per frame update
        self.orbit_rad = rad[1]
        self.orbit_center = (pos[0] , pos[1])

    # check if target is touching orb
    def check(self, orb):
        if self.exists:
            dist_x = orb.pos_x - self.pos_x
            dist_y = orb.pos_y - self.pos_y
            dist_tot = math.sqrt(dist_x ** 2 + dist_y ** 2)
            if dist_tot <= self.rad + orb.rad:
                orb.colour = colours.WIN_YELLOW
                #sounds.play_sound('target_sound.wav')
                self.exists = 0
                return 1
            else:
                return 0

    # update target position
    def update(self, size):
        if self.exists:
            # now shuffle it along
            self.orbit_center = (self.orbit_center[0] + self.vel_x , self.orbit_center[1] + self.vel_y)
            # pac man this bitch
            if self.orbit_center[1] < -self.orbit_rad:
                self.orbit_center = (self.orbit_center[0] , size[1] + self.orbit_rad)
            if self.orbit_center[1] > size[1] + self.orbit_rad:
                self.orbit_center = (self.orbit_center[0] , -self.orbit_rad)
            if self.orbit_center[0] < -self.orbit_rad:
                self.orbit_center = (size[0] + self.orbit_rad , self.orbit_center[1])
            if self.orbit_center[0] > size[0] + self.orbit_rad:
                self.orbit_center = (-self.orbit_rad , self.orbit_center[1])
            # now circular motion
            self.theta = self.theta + self.vel_circ
            self.pos_x = self.orbit_center[0] + int(self.orbit_rad * math.cos(self.theta))
            self.pos_y = self.orbit_center[1] + int(self.orbit_rad * math.sin(self.theta))

    # draw target to screen
    def draw(self, screen):
        if self.exists:
            pygame.draw.circle(screen, self.colour, (self.pos_x, self.pos_y), self.rad, 0)
