"""Advent of Code 2020 day 5 part 1"""

def find_seat(sequence: str) -> int:
    """"Find the seat by parsing the sequence"""
    row_sequence = sequence[:7]
    column_sequence = sequence[7:10]
    # print(row_sequence)
    # print(column_sequence)

    r_start = 0
    r_end = 127
    for step in row_sequence:
        # print(f"start: {r_start} & end: {r_end}")
        if step == 'F':
            r_end = int((r_end-r_start)/2) + r_start - 1
        else: #step == 'B'
            r_start = int((r_end-r_start)/2) + r_start + 1
    # print(f"start: {r_start} & end: {r_end}")
    found_row = r_start
    # print(f"found row {found_row}")

    c_start = 0
    c_end = 7
    for step in column_sequence:
        # print(f"start: {c_start} & end: {c_end}")
        if step == 'L':
            c_end = int((c_end-c_start)/2) + c_start - 1
        else: #step == 'R'
            c_start = int((c_end-c_start)/2) + c_start + 1
    # print(f"start: {c_start} & end: {c_end}")
    found_col = c_start
    # print(f"found col {found_col}")

    return found_row * 8 + found_col

def find_seat_cheater(sequence: str) -> int:
    """Takes advantage of the fact that the sequence is basicaly a binary number"""
    return int(sequence.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2)


def main():
    """The main method"""
    boarding_passes = []
    with open('day5/input.txt') as f:
        boarding_passes = f.read().splitlines()

    seats = []
    for boarding_pass in boarding_passes:
        seats.append(find_seat(boarding_pass))

    print(max(seats))
    # print(str(seats))


if __name__ == "__main__":
    # execute only if run as a script
    main()
