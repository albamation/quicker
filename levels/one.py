import sys, pygame, math
from constants import settings, colours

sys.path.insert(0, '../shapes/orbs/Orb')
sys.path.insert(0, '../shapes/targets/Target')
sys.path.insert(0, '../shapes/obstacles/Obstacle')

from Cursor import Cursor
from Orb import Orb
from Target import Target
from Obstacle import Obstacle
from Supertarget import Supertarget

# cursor initialization variables
cursor_mass_start = 5000
cursor_rad = 50

# orb initialization variables
orb_pos_start = (560, 400)
orb_rad = 20
orb_colour = colours.WHITE

# obstacle initialization variables
obstacle_rad = (10 , 200)
obstacle_pos = (600, 400, 0)
obstacle_vel = (0, 0, 6)

# target initialization variables
target_rad = (10 , 150)
target_pos = (500, 300, 0)
target_vel = (1, 1, 10)

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
                        (200,300, 0), # start position (x,y)
                        (15,0),    # radius (size, orbit)
                        (-2,3,0)   # velocity (x,y,circular)
                        ),

                Target(
                        (800,500, 0),  # start position (x,y)
                        (25,50),    # radius (size, orbit)
                        (0,5,10)    # velocity (x,y,circular)
                        ),

                ],

    'supertargets' : [
                # Supertarget(
                #         (200,100, 0), # start position (x,y, angle in degrees)
                #         (10, 0),    # radius (size, orbit)
                #         (0, 0, 0)   # velocity (x,y,circular)
                #         ),
                #
                # Supertarget(
                #         (1000,700, 0), # start position (x,y, angle in degrees)
                #         (10, 0),    # radius (size, orbit)
                #         (0, 0, 0)   # velocity (x,y,circular)
                #         ),
                ],

    'obstacles' : [
                Obstacle(
                        obstacle_pos,
                        obstacle_rad,
                        obstacle_vel
                        ),

                Obstacle(
                        (700,500,0),  # start position (x,y)
                        (50,50),    # radius (size, orbit)
                        (-3,5,5)    # velocity (x,y,circular)
                        ),
                ]
}
