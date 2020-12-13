from enum import Enum

class Waypoint:

    def __init__(self):
        self.ew = 10
        self.ns = 1
        self.manuvers = 0

    def __str__(self):
        ew_dir = 'EAST'
        if self.ew < 0:
            ew_dir = 'WEST'
        ns_dir = 'NORTH'
        if self.ns < 0:
            ns_dir = 'SOUTH'
        return f"Waypoint is currently at position {abs(self.ew)} {ew_dir} & {abs(self.ns)} {ns_dir}"

    def manhattan_distance(self):
        return abs(self.ns) + abs(self.ew)

    def north(self, val):
        self.ns += val
        # print(self)
    def south(self, val):
        self.ns -= val
        # print(self)
    def east(self, val):
        self.ew += val
        # print(self)
    def west(self, val):
        self.ew -= val
        # print(self)

    def right(self, val):
        if val == 90:
            new_ns = -1*self.ew
            new_ew = self.ns
            self.ns = new_ns
            self.ew = new_ew
        elif val == 180:
            self.ew = -1*self.ew
            self.ns = -1*self.ns
        elif val == 270:
            new_ew = -1*self.ns
            new_ns = self.ew
            self.ew = new_ew
            self.ns = new_ns
        # print(f"[{self.manuvers}] Current direction {current_val}, moving right {val} and new value {next_val} direction {self.direction}")

    def left(self, val):
        if val == 90:
            new_ns = self.ew
            new_ew = -1*self.ns
            self.ns = new_ns
            self.ew = new_ew
        elif val == 180:
            self.ew = -1*self.ew
            self.ns = -1*self.ns
        elif val == 270:
            new_ns = -1*self.ew
            new_ew = self.ns
            self.ns = new_ns
            self.ew = new_ew
        # print(f"[{self.manuvers}] Current direction {current_val}, moving left {val} and new value {next_val} direction {self.direction}")

class Ship():

    def __init__(self):
        self.ew = 0
        self.ns = 0

    def forward(self, waypoint: Waypoint, value):
        self.ew += waypoint.ew * value
        self.ns += waypoint.ns * value

    def __str__(self):
        ew_dir = 'EAST'
        if self.ew < 0:
            ew_dir = 'WEST'
        ns_dir = 'NORTH'
        if self.ns < 0:
            ns_dir = 'SOUTH'
        return f"Ship is currently at position {abs(self.ew)} {ew_dir} & {abs(self.ns)} {ns_dir}"

    def manhattan_distance(self):
        return abs(self.ns) + abs(self.ew)