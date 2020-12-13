"""Advent of Code 2020 day 12 part 2"""

from waypoint import Ship, Waypoint

def main():
    commands = []
    with open('day12/input.txt', 'r') as f:
        commands = f.read().splitlines()

    ship = Ship()
    waypoint = Waypoint()

    pair = (waypoint, ship)
    for command in commands:
        execute_command(actor=pair, command=command)

    print(ship)
    print(f"Manhattan distance {ship.manhattan_distance()}")


def execute_command(command: str, actor: (Waypoint, Ship)):
    waypoint = actor[0]
    ship = actor[1]
    operation = command[0]
    value = int(command[1:])

    if operation == 'F':
        ship.forward(waypoint, value)
    elif operation == 'N':
        waypoint.north(value)
    elif operation == 'E':
        waypoint.east(value)
    elif operation == 'S':
        waypoint.south(value)
    elif operation == 'W':
        waypoint.west(value)
    elif operation == 'L':
        waypoint.left(value)
    elif operation == 'R':
        waypoint.right(value)
    else:
        print(f"Invalid syntax with command {command}")

if __name__ == '__main__':
    main()