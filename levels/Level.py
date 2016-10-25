# parent level class
class Level:

    cursor = False;
    orbs = [];
    targets = [];
    obstacles = [];

    # load up a specific level
    def __init__(self, level):
        self.cursor = level['cursor']
        self.orbs = level['orbs']
        self.targets = level['targets']
        self.obstacles = level['obstacles']

    # check if the player is boosting (5 = down, 6 = up)
    # NOTE: this doesn't work with multiple orbs right now
    def check_boost(self, event):
        for orb in self.orbs:
            if (event == 5): # boosting
                orb.cursor.mass = orb.cursor.mass_start + orb.cursor.mass_boost
                return True
            if (event == 6): # not boosting
                orb.cursor.mass = orb.cursor.mass_start
                return False

    # check if an orb hits the screen boundary
    def check_boundary(self, boundary):
        for orb in self.orbs:
            if boundary.collidepoint(orb.pos_x, 0) == 0:
                orb.vel_x = -orb.vel_x
            if boundary.collidepoint(0, orb.pos_y) == 0:
                orb.vel_y = -orb.vel_y

    # check if an orb is within radius of the cursor
    def check_cursor(self):
        for orb in self.orbs:
            if orb.cursor_dist_tot <= orb.cursor.rad:
                orb.pos_x = orb.pos_start[0]
                orb.pos_y = orb.pos_start[1]

    # check if targets/obstacles are touching orbs
    def check(self):
        for orb in self.orbs:
            for target in self.targets:
                target.check(orb)
            for obstacle in self.obstacles:
                obstacle.check(orb)

    # update shape positions
    def update(self, screen_size):
        for orb in self.orbs:
            orb.update()
        for target in self.targets:
            target.update(screen_size)
        for obstacle in self.obstacles:
            obstacle.update(screen_size)

    # draw shapes to screen
    def draw(self, screen):
        for orb in self.orbs:
            orb.draw(screen)
        for target in self.targets:
            target.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
