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
orb_rad = 20
orb_pos_start = (600, 400)
orb_colour = colours.WHITE

# obstacle initialization variables
obstacle_rad = (10 , 100)      #radius (size, orbit)
obstacle_pos = (600, 400, 0) #(x, y, start angle in degrees)
obstacle_vel = (0, 0, 1)       #velocity (x,y,circular: +CW,-CCW)

# target initialization variables
target_rad = (10 , 200)     #radius (size, orbit)
target_pos = (600, 400, 180)  #(x, y, start angle in degrees)
target_vel = (0, 0, -2)     #velocity (x,y,circular: +CW,-CCW)

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
                        target_pos, # start position (x,y, start angle in degrees)
                        (target_rad[0], 400),    # radius (size, orbit)
                        (target_vel[0], target_vel[1], -4)   # velocity (x,y,circular: +CW,-CCW)
                        ),
                #
                # Target(
                #         (750,400), # start position (x,y)
                #         target_rad,    # radius (size, orbit)
                #         target_vel   # velocity (x,y,circular: +CW,-CCW)
                #         ),
                #
                # Target(
                #         (1050,400), # start position (x,y)
                #         target_rad,    # radius (size, orbit)
                #         target_vel   # velocity (x,y,circular: +CW,-CCW)
                #         ),

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
                        obstacle_pos,  # start position (x,y)
                        (obstacle_rad[0], 300),    # radius (size, orbit)
                        (obstacle_vel[0], obstacle_vel[1], 3)   # velocity (x,y,circular: +CW,-CCW)
                        ),
                #
                # Obstacle(
                #         (500,0),  # start position (x,y)
                #         obstacle_rad,    # radius (size, orbit)
                #         (0,-2,0)   # velocity (x,y,circular: +CW,-CCW)
                #         ),
                #
                # Obstacle(
                #         (800,0),  # start position (x,y)
                #         obstacle_rad,    # radius (size, orbit)
                #         (0,3,0)   # velocity (x,y,circular: +CW,-CCW)
                #         ),
                #
                # Obstacle(
                #         (700,0),  # start position (x,y)
                #         obstacle_rad,    # radius (size, orbit)
                #         (0,-4,0)   # velocity (x,y,circular: +CW,-CCW)
                #         ),
                #
                # Obstacle(
                #         (1000,0),  # start position (x,y)
                #         obstacle_rad,    # radius (size, orbit)
                #         (0,-5,0)   # velocity (x,y,circular: +CW,-CCW)
                #         ),
                ]
}
