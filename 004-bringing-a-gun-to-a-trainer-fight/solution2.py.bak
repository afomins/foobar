from array import *
import fractions
import math

nolog = 0

def log(s):
    if nolog:
        return
    print(s)

class Utils:
    squares = None
    gcd = None

    @staticmethod
    def init(squares_max):
        Utils.squares = array('L', [i * i for i in range(squares_max + 1)])
        Utils.gcd = dict()

    @staticmethod
    def get_gcd(x, y):
        x = abs(x)
        y = abs(y)

        if x == y:
            return 0 if x == 0 else x

        key = (x, y) if x < y else (y, x)
        if key in Utils.gcd:
            return Utils.gcd[key]
        else:
            val = Utils.gcd[key] = fractions.gcd(x, y)
            return val

class Vector:
    def __init__(self, pos_x, pos_y):
        self.x = float(pos_x)
        self.y = float(pos_y)

class Ray:
    def __init__(self, origin, dir):
        # GDC-normalized direction
        self.dir = dir

        # Vertical/horizontal
        if self.is_vertical() or self.is_horizontal():
            self.b = 0.0

        # Skewed line equasion: y = a * x + b
        #  a = dir.y / dir.x
        #  b = origin.y - a * origin.x
        else:
            self.b = origin.y - ((origin.x * dir.y) / dir.x)

    def is_vertical(self):
        return self.dir.x == 0

    def is_horizontal(self):
        return self.dir.y == 0

    def get_key(self):
        return (self.dir.x, self.dir.y, self.b)

    def get_str(self):
        return "(" + str(self.dir.x) + "," + str(self.dir.y) + "," + str(self.b) + ")"

    def get_normalized_dir(self):
        dx = self.dir.x
        dy = self.dir.y
        len = math.sqrt(dx * dx + dy * dy)
        return Vector(dx / len, dy / len)

class Room:
    def __init__(self, size, origin, target):
        self.size = size
        self.origin = origin
        self.target = target

    def test_segment(self, x, y, ray):
        pass

    def shoot(self, ray, distance):
        def test_straight_line(origin, len, dir, target):
            if dir > 0: # right/up
                return origin + len >= target
            else: # left/down
                return origin - len <= target

        #
        # Vertical
        #
        if ray.is_vertical():
            return self.origin.x == self.target.x and \
                test_straight_line(self.origin.y, distance, ray.dir.y, self.target.y)

        #
        # Horizontal
        #
        if ray.is_horizontal():
            return self.origin.y == self.target.y and \
                test_straight_line(self.origin.x, distance, ray.dir.x, self.target.x)

        #
        # Skewed
        #
        dir_norm = ray.get_normalized_dir()
        end_of_ray = Vector(self.origin.x + dir_norm.x * distance, \
                            self.origin.y + dir_norm.y * distance)
        last_segment_idx = int(end_of_ray.x / self.size.x)

        for segment_x in range(last_segment_idx + 1):
            cross_x = float(segment_x * self.size.x)
            if segment_x % 2 == 0: # even
                cross_x += self.target.x # normal offset

            else: # odd
                cross_x += self.size.x - self.target.x # mirror offset

            # a = dir.y / dir.x
            # y = x * a + b
            cross_y = (cross_x * dir_norm.y) / dir_norm.x + ray.b

        return False


def solution(dimensions, your_position, trainer_position, distance):
    # Initialize
    Utils.init(distance + 1)

    # Prepare level
    room_size = Vector(dimensions[0], dimensions[1])
    origin = Vector(your_position[0], your_position[1])
    target = Vector(trainer_position[0], trainer_position[1])
    room = Room(room_size, origin, target)

    # Cache
    rays = dict()
    rays_hits = []

    # Iterate all possible vectors
    for y in range(distance):
        for x in range(distance):
            if x == y == 0:
                continue # ignore self

            # Perfectly, fucking, vertical
            if x == 0: 
                dir_x = 0
                dir_y = 1 if y > 0 else -1

            # Horizontal
            elif y == 0: 
                dir_x = 1 if x > 0 else -1
                dir_y = 0

            # Simplify skewed vector by greatest-common-divisor
            else:
                gcd = Utils.get_gcd(x, y)
                dir_x = x / gcd
                dir_y = y / gcd

            # Create and cache new ray
            ray = Ray(origin, Vector(dir_x, dir_y))
            ray_key = ray.get_key()
            if ray_key in rays:
                d = rays[ray_key]
                log("v=(" + str(x) + "," + str(y) + ") duplicate by " + d.get_str())
                continue # ignore duplicate
            else:
                rays[ray_key] = ray

            # Shoot
            rc = room.shoot(ray, distance)
            if rc:
                rays_hits.append(ray)

            log("v=(" + str(x) + "," + str(y) + ") -> " + ray.get_str() + " rc=" + str(rc))

    log("")
    log("Hits=" + str([(r.dir.x, r.dir.y, r.b) for r in rays_hits]))
    return len(rays_hits)
