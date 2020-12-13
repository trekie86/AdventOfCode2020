from enum import Enum

class Boat:

    def __init__(self):
        self.direction = Compass.EAST
        self.ew = 0
        self.ns = 0
        self.manuvers = 0

    def __str__(self):
        ew_dir = 'EAST'
        if self.ew < 0:
            ew_dir = 'WEST'
        ns_dir = 'NORTH'
        if self.ns < 0:
            ns_dir = 'SOUTH'
        return f"[{self.manuvers}] Boat is currently facing {self.direction} at position {abs(self.ew)} {ew_dir} & {abs(self.ns)} {ns_dir}"

    def manhattan_distance(self):
        return abs(self.ns) + abs(self.ew)

    def north(self, val):
        self.ns += val
        self.manuvers += 1
        print(self)
    def south(self, val):
        self.ns -= val
        self.manuvers += 1
        print(self)
    def east(self, val):
        self.ew += val
        self.manuvers += 1
        print(self)
    def west(self, val):
        self.ew -= val
        self.manuvers += 1
        print(self)

    def forward(self, val):
        if self.direction == Compass.EAST:
            self.ew += val
        elif self.direction == Compass.WEST:
            self.ew -= val
        elif self.direction == Compass.NORTH:
            self.ns += val
        elif self.direction == Compass.SOUTH:
            self.ns -= val
        else:
            print(f"This should never happen.")
        self.manuvers += 1
        print(self)

    def right(self, val):
        current_val = self.direction.value
        next_val = (current_val + val) % 360
        self.direction = Compass(next_val)
        self.manuvers += 1
        print(f"[{self.manuvers}] Current direction {current_val}, moving right {val} and new value {next_val} direction {self.direction}")

    def left(self, val):
        current_val = int(self.direction.value)
        next_val = (current_val - val + 360) % 360
        self.direction = Compass(next_val)
        self.manuvers += 1
        print(f"[{self.manuvers}] Current direction {current_val}, moving left {val} and new value {next_val} direction {self.direction}")

class Compass(Enum):
    NORTH = 0
    SOUTH = 180
    EAST = 90
    WEST = 270