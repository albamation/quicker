import sys, pygame, math
from constants import settings, colours

sys.path.insert(0, '../shapes/orbs/Orb')
sys.path.insert(0, '../shapes/targets/Target')
sys.path.insert(0, '../shapes/obstacles/Obstacle')
sys.path.insert(0, '../shapes/supertargets/Supertarget')

from Cursor import Cursor
from Orb import Orb
from Target import Target
from Obstacle import Obstacle
from Supertarget import Supertarget

# cursor initialization variables
cursor_mass_start = 5000
cursor_rad = 50

# orb initialization variables
orb_rad = 20
orb_pos_start = (orb_rad, 400)
orb_colour = colours.WHITE

# obstacle initialization variables
obstacle_rad = (10 , 0)
obstacle_pos = (200,800, 0)
obstacle_vel = (0, -1, 0)

# target initialization variables
target_rad = (10 , 30)
target_pos = (150, 400, 0)
target_vel = (0, 0, 3)

# instantiate cursor
cursor = Cursor(cursor_rad, cursor_mass_start)

# define level dictionary
level = {
    'cursor' : cursor,
    'orbs' : [Orb(orb_pos_start, orb_rad, orb_colour, cursor)],

    'targets' : [
                Target(
                         target_pos,
                         target_rad,
                         target_vel
                         ),

                Target(
                        (450,400, 90), # start position (x,y)
                        target_rad,    # radius (size, orbit)
                        target_vel   # velocity (x,y,circular)
                        ),

                Target(
                        (750,400, 180), # start position (x,y)
                        target_rad,    # radius (size, orbit)
                        target_vel   # velocity (x,y,circular)
                        ),

                Target(
                        (1050,400, 270), # start position (x,y)
                        target_rad,    # radius (size, orbit)
                        target_vel   # velocity (x,y,circular)
                        ),

                ],

    'supertargets' : [
                Supertarget(
                        (200,100, 0), # start position (x,y, angle in degrees)
                        (10, 0),    # radius (size, orbit)
                        (0, 0, 0)   # velocity (x,y,circular)
                        ),

                Supertarget(
                        (1000,700, 0), # start position (x,y, angle in degrees)
                        (10, 0),    # radius (size, orbit)
                        (0, 0, 0)   # velocity (x,y,circular)
                        ),
                ],

    'obstacles' : [
                Obstacle(
                        obstacle_pos,
                        obstacle_rad,
                        obstacle_vel
                        ),

                Obstacle(
                        (400,0, 0),  # start position (x,y)
                        obstacle_rad,    # radius (size, orbit)
                        (0,1,0)   # velocity (x,y,circular)
                        ),

                Obstacle(
                        (500,0, 0),  # start position (x,y)
                        obstacle_rad,    # radius (size, orbit)
                        (0,-2,0)   # velocity (x,y,circular)
                        ),

                Obstacle(
                        (800,0, 0),  # start position (x,y)
                        obstacle_rad,    # radius (size, orbit)
                        (0,3,0)   # velocity (x,y,circular)
                        ),

                Obstacle(
                        (700,0, 0),  # start position (x,y)
                        obstacle_rad,    # radius (size, orbit)
                        (0,-4,0)   # velocity (x,y,circular)
                        ),

                Obstacle(
                        (1000,0, 0),  # start position (x,y)
                        obstacle_rad,    # radius (size, orbit)
                        (0,-5,0)   # velocity (x,y,circular)
                        ),
                ]
}
