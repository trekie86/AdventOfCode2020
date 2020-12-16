"""Advent of Code 2020 day 13 part 2"""

"""This solution is garbage and either doesn't work or won't in a timely manner"""

import numpy as np
import math

def main():
    with open('day13/input.txt', 'r') as f:
        raw_input = f.read().splitlines()
        busses = np.array(raw_input[1].split(','))

    print(f"Available busses: {busses}")

    first_time = find_subsequent_busses(busses)
    print(f"Earliest subsequent timestamp: {first_time}")


def find_subsequent_busses(busses):
    idx = 1
    multipliers = np.ones(len(busses))
    #Found the LCM of the numbers
    first_real_numbers = [int(x) for x in busses if x != 'x']
    multipliers[0] = first_real_numbers[0]*first_real_numbers[1]
    count = 0
    while idx < len(busses):
        if count % 1000000 == 0:
            print(f"Current start time at {'{:,}'.format(int(busses[0])*multipliers[0])}")
        #Assuming index 0 is a number and not 'x'
        if busses[idx] == 'x':
            #Nothing to do here, check the next value
            idx += 1
            count += 1
            #I don't think this continue is really necessary
            continue
        else:
            if int(busses[0])*multipliers[0] + idx == int(busses[idx]) * multipliers[idx]:
                #This is a good condition where we have are on the right track
                idx += 1
                count += 1
                continue
            elif int(busses[0])*multipliers[0] + idx < int(busses[idx]) * multipliers[idx]:
                #The starting position of index 0 is too low, need to bump up and loop again
                multipliers[0] += 1
                idx = 1
                count += 1
                #Start the loop again
                continue
            else: #The next value is too low, we need to bump up value of busses[idx]
                while int(busses[0])*multipliers[0] + idx > int(busses[idx]) * multipliers[idx]:
                    if (int(busses[0])*multipliers[0] + idx) - (int(busses[idx]) * multipliers[idx]) > int(busses[idx]):
                        multipliers[idx] = int((int(busses[0])*multipliers[0] + idx) / int(busses[idx]))
                    else:
                        multipliers[idx] += 1
                    count += 1
                    #This will loop until the value goes up and then evaluate again starting at the same point
                    #If it meets the criteria, the index will move up to the next value, if it's now too large,
                    # the loop will start over again from 1
                #This probably isn't necessary
                continue
    #We have reached the happy place
    return int(int(busses[0])*multipliers[0])






if __name__ == '__main__':
    main()