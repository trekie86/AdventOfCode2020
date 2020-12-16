"""Advent of Code 2020 day 15 part 1"""
from collections import defaultdict

def main():

    stop_step = 30000000

    with open('day15/sample.txt', 'r') as f:
        inputs = f.read().splitlines()[0].split(',')

    last_spoken = loop_interactions(inputs, stop_step)
    print(f"At position {stop_step} the value spoken is {last_spoken}")

def loop_interactions(inputs, stop_step):
    spoken_map = {}
    last_spoken = None
    step = 1
    for val in inputs:
        spoken_map[int(val)] = [step]
        step += 1
        last_spoken = int(val)

    for step in range(len(inputs)+1, stop_step + 1):
        last_spoken_list = spoken_map.get(last_spoken, [])
        if len(last_spoken_list) == 1:
            #This number has only been spoken before, so it was the first time it had been spoken
            #Since that is the case, the number spoken is now 0
            last_spoken = 0
            last_spoken_list = spoken_map.get(last_spoken, [])
            last_spoken_list.append(step)
            spoken_map[last_spoken] = last_spoken_list
        elif len(last_spoken_list) > 1:
            #This number has been spoken before, so take the subtraction of the last two times spoken and that is the new number spoken
            last_spoken = last_spoken_list[-1] - last_spoken_list[-2]
            last_spoken_list = spoken_map.get(last_spoken, [])
            last_spoken_list.append(step)
            spoken_map[last_spoken] = last_spoken_list[-2:]

    return last_spoken

if __name__ == '__main__':
    main()