"""Advent of Code 2020 day 12 part 1"""

from boat import Boat

def main():
    commands = []
    with open('day12/input.txt', 'r') as f:
        commands = f.read().splitlines()

    boat = Boat()

    for command in commands:
        execute_command(actor=boat, command=command)

    print(boat)
    print(f"Manhattan distance {boat.manhattan_distance()}")

def execute_command(command: str, actor: Boat):
    operation = command[0]
    value = int(command[1:])

    if operation == 'F':
        actor.forward(value)
    elif operation == 'N':
        actor.north(value)
    elif operation == 'E':
        actor.east(value)
    elif operation == 'S':
        actor.south(value)
    elif operation == 'W':
        actor.west(value)
    elif operation == 'L':
        actor.left(value)
    elif operation == 'R':
        actor.right(value)
    else:
        print(f"Invalid syntax with command {command}")

if __name__ == '__main__':
    main()
