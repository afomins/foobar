from array import *
#import fractions
#import math

nolog = 0

def log(s):
    if nolog:
        return
    print(s)

class Utils:
    squares = None
    # gcd = None

    @staticmethod
    def init(squares_max):
        # Lookup table for squares
        Utils.squares = array('L',
            [i * i for i in range(squares_max + 1)])

        # Cache for GCD values
        Utils.gcd = dict()

    @staticmethod
    def get_square(val):
        try:
            return Utils.squares[abs(val)]
#            return val * val
        except:
            log("Failed to find square for " + str(val) + " :: max=" + str(len(Utils.squares)))
            return None

#    @staticmethod
#    def get_gcd(x, y):
#        x = abs(x)
#        y = abs(y)
#
#        if x == y:
#            return 0 if x == 0 else x
#
#        key = (x, y) if x < y else (y, x)
#        if key in Utils.gcd:
#            return Utils.gcd[key]
#        else:
#            val = Utils.gcd[key] = fractions.gcd(x, y)
#            return val

class Vector2i:
    def __init__(self, x = 0, y = 0):
        self.x = int(x)
        self.y = int(y)

    def str(self):
        return str((self.x, self.y))

class Line:
    def __init__(self, eol):
        # End of line
        self.eol = eol

        #
        # Line equasion             -> y = a * x + b
        # For lines crossing (0, 0) -> b = 0
        #                           -> a = y / x
        #

        # Perfectly, fucking, vertical line
        if self.is_vertical():
            self.a = float('inf')

            # Normalized direction
#            self.dir = Vector2i(0, +1 if eol.y > 0 else -1)

        # Horizontal line
        elif self.is_horizontal():
            self.a = 0.0

            # Normalized direction
#            self.dir = Vector2i(+1 if eol.x > 0 else -1, 0)

        # Skewed line
        else:
            self.a = float(eol.y) / float(eol.x)

            # Normalized direction
#            gcd = Utils.get_gcd(eol.x, eol.y)
#            self.dir = Vector2i(eol.x / gcd, eol.y / gcd)

        # Length of the line squared
        self.len2 = \
            Utils.get_square(eol.x) + Utils.get_square(eol.y)

        # Quater where eol resides:
        #      ^
        #    2 | 1
        # -----+--->
        #    3 | 4
        self.quater = \
            1 if eol.x >  0 and eol.y >= 0 else \
            2 if eol.x <= 0 and eol.y >  0 else \
            3 if eol.x <  0 and eol.y <= 0 else \
            4 if eol.x >= 0 and eol.y <  0 else \
            42 # should not happen

    def is_vertical(self):
        return self.eol.x == 0

    def is_horizontal(self):
        return self.eol.y == 0

    def get_key(self):
        return (self.a, self.quater)
#        return (self.dir.x, self.dir.y, self.quater)

    def str(self):
        return \
             "(x=" + str(self.eol.x) + \
            ", y=" + str(self.eol.y) + \
            ", l=" + str(self.len2) + \
            ", q=" + str(self.quater) + \
            ", a=" + str(self.a) + ")"

class Room:
    def __init__(self, x, y, size, offset):
        # Index of the room in each direction
        self.idx = Vector2i(x, y)

        # Size of the room
        self.size = size

        # Invert room layout per-axis for odd rooms
        self.invert = Vector2i(x % 2, y % 2)

        # Coordinates of bottom-left corner of the room
        self.pos = Vector2i(
            x * size.x - offset.x,
            y * size.y - offset.y)

    def get_aligned_pos(self, pos):
        def align(pos, origin, size, invert):
            if invert == 0:
                return origin + pos
            else:
                return origin + size - pos

        return Vector2i(
            align(pos.x, self.pos.x, self.size.x, self.invert.x),
            align(pos.y, self.pos.y, self.size.y, self.invert.y));

def solution(dimensions, your_position, trainer_position, distance):
    # Prepare level
    room_size = Vector2i(dimensions[0], dimensions[1])
    player_pos = Vector2i(your_position[0], your_position[1])
    enemy_pos = Vector2i(trainer_position[0], trainer_position[1])

    # Number of rooms expanded in each direction
    room_num = Vector2i(distance / room_size.x + 1, \
                        distance / room_size.y + 1)

    # Init
    Utils.init(max(
        (room_num.x + 1) * room_size.x, 
        (room_num.y + 1) * room_size.y))

    log("room-size      -> " + room_size.str())
    log("room-expansion -> " + room_num.str())
    log("player-pos     -> " + player_pos.str())
    log("enemy-pos      -> " + enemy_pos.str())
    log("ray-distance   -> " + str(distance))
    log("")

    # Distance squared
    distance2 = Utils.get_square(distance)

    # Check if too far
    origin_room = Room(0, 0, room_size, player_pos)
    enemy_pos_aligned = origin_room.get_aligned_pos(enemy_pos);
    stright_line_to_enemy = Line(enemy_pos_aligned)
    if stright_line_to_enemy.len2 > distance2:
        log(" line=" + stright_line_to_enemy.str() + \
            " room=" + origin_room.idx.str() + \
            " TOO FAR")
        return 0

    # Check if exact match
    if stright_line_to_enemy.len2 == distance2:
        log(" line=" + stright_line_to_enemy.str() + \
            " room=" + origin_room.idx.str() + \
            " EXACT MATCH")
        return 1

    # Room generator
    def walk_rooms(num, size, offset):
        for y in range(-num.y, +num.y + 1):
            for x in range(-num.x, +num.x + 1):
                yield Room(x, y, size, offset);

    #
    # Cache all lines from player in room (0, 0) to enemies in all extended rooms
    #
    log("Targeting enemies:")
    enemies = dict();
    for room in walk_rooms(room_num, room_size, player_pos):
        # Position of the enemy in extended room
        aligned_pos = room.get_aligned_pos(enemy_pos)

        # Ignore origin
        if aligned_pos.x == aligned_pos.y == 0:
            continue

        # Build new line from player (0, 0) to enemy in extended room
        line = Line(aligned_pos)

        # Ignore candidates past max distance
        if (line.len2 > distance2):
            continue

        # Cache unique line
        line_key = line.get_key()
        line_cached = enemies[line_key] if line_key in enemies else None
        line_status = ""
        if line_cached == None:
            enemies[line_key] = line
            line_status = "NEW"

        # Prefer shorter lines
        else:
            if line.len2 < line_cached.len2:
                enemies[line_key] = line
                line_status = "UPDATE-SHORTER-LENGTH"
            else:
                line_status = "IGNORE"

        log(" line=" + line.str() +
            " room=" + room.idx.str() +
            " " + line_status)

    #
    # Remove lines colliding with players in extended rooms
    #
    log("")
    log("Targeting players:")
    for room in walk_rooms(room_num, room_size, player_pos):
        # Position of the player in extended room
        aligned_pos = room.get_aligned_pos(player_pos)

        # Ignore room (0, 0)
        if room.idx.x == room.idx.y == 0:
            continue

        # Build new line from player (0, 0) to player in extended room
        line = Line(aligned_pos)

        # Remove collisions from cache
        line_key = line.get_key()
        line_cached = enemies[line_key] if line_key in enemies else None
        if line_cached == None:
            continue

        if line.len2 < line_cached.len2:
            del enemies[line_key]
            log(" line=" + line.str() +
                " room=" + room.idx.str() +
                " DETECTED-PLAYER-COLLISION")

    log("")
    log("Done")
#    log("" + str([l.str() for l in enemies.values()]))
    return len(enemies)
