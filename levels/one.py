import sys, pygame, math
from constants import settings, colours

sys.path.insert(0, '../shapes/orbs/Orb')
sys.path.insert(0, '../shapes/targets/Target')
sys.path.insert(0, '../shapes/obstacles/Obstacle')

from Cursor import Cursor
from Orb import Orb
from Target import Target
from Obstacle import Obstacle

# cursor initialization variables
cursor_mass_start = 5000
cursor_rad = 50

# orb initialization variables
orb_pos_start = (100, 200)
orb_rad = 20
orb_colour = colours.WHITE

# obstacle initialization variables
obstacle_rad = 20
obstacle_pos = (500,500)
obstacle_vel = (1, 1)

# target initialization variables
target_rad = 10
target_pos = (1100, settings.screen_size[1] + target_rad)
target_vel = (1, 1, 0)

# instantiate cursor
cursor = Cursor(cursor_rad, cursor_mass_start)

# define level dictionary
level = {
    'cursor' : cursor,
    'orbs' : [Orb(orb_pos_start, orb_rad, orb_colour, cursor)],
    'targets' : [Target(target_pos, target_rad, target_vel, 0),
                 Target((0, 0), target_rad, (0, 0, 2*math.pi/120), 20),
                 Target((700, settings.screen_size[1] + target_rad + 5), target_rad + 10, (1, 4, 0), 0)],
    'obstacles' : [Obstacle(obstacle_pos, obstacle_rad, obstacle_vel, "ltr", 0),
                   Obstacle((settings.screen_size[0] + obstacle_rad - 500, 400), obstacle_rad, obstacle_vel, "cw", 50),
                   Obstacle((500, 500), obstacle_rad, (1,1), "ccw", 200)]
}
