"""Advent of Code 2020 day 13 part 1"""

def main():
    with open('day13/input.txt', 'r') as f:
        raw_input = f.read().splitlines()
        departure = int(raw_input[0])
        busses = [int(bus) for bus in raw_input[1].split(',') if bus != 'x']

    print(f"Earliest departure time {departure}")
    print(f"Available busses: {busses}")

    bus_options = find_earlist_busses(departure=departure, busses=busses)

    bus_options.sort(key=lambda x: x[1])
    print(f"Sorted bus schedule {bus_options}")

    earliest_bus = bus_options[0][0]
    earliest_time = bus_options[0][1]

    print(earliest_bus*(earliest_time-departure))

def find_earlist_busses(departure, busses) -> []:
    bus_options = []
    for bus in busses:
        depart_time = 0
        while depart_time < departure:
            depart_time += bus
        bus_options.append((bus, depart_time))

    print(f"Available departure options: {bus_options}")
    return bus_options

if __name__ == '__main__':
    main()