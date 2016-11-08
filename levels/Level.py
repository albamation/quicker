from sounds import sounds
# parent level class
class Level:

    cursor = False;
    orbs = [];
    targets = [];
    obstacles = [];
    supertargets = [];
    points = 0;
    level_complete = 0;

    # load up a specific level
    def __init__(self, level):
        self.cursor = level['cursor']
        self.orbs = level['orbs']
        self.targets = level['targets']
        self.obstacles = level['obstacles']
        self.supertargets = level['supertargets']

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
                self.points = self.points - 1
                sounds.play_sound('sounds/cursor_hit_sound.wav')

    # check if targets/obstacles are touching orbs
    def check(self):
        for orb in self.orbs:
            for target in self.targets:
                if target.check(orb):
                    self.points = self.points + 1
            for obstacle in self.obstacles:
                if obstacle.check(orb):
                    self.points = self.points - 1
            for supertarget in self.supertargets:
                if supertarget.check(orb):
                    self.points = self.points + 3

    # check if all targets have been collected
    def level_check(self):
        number_targets = len(self.targets)
        target_check = 0
        for target in self.targets:
            if target.exists == 0:
                target_check = target_check + 1
        if target_check == number_targets:
            self.level_complete = 1
        return self.level_complete

    # update shape positions
    def update(self, screen_size):
        for orb in self.orbs:
            orb.update()
        for target in self.targets:
            target.update(screen_size)
        for obstacle in self.obstacles:
            obstacle.update(screen_size)
        for supertarget in self.supertargets:
            supertarget.update(screen_size)

    # draw shapes to screen
    def draw(self, screen):
        for orb in self.orbs:
            orb.draw(screen)
        for target in self.targets:
            target.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        for supertarget in self.supertargets:
            supertarget.draw(screen)
