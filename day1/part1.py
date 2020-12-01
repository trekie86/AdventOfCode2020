from itertools import combinations
from math import prod

inputLines = []
with open("./part1input.txt", "r") as f:
    for line in f:
        inputLines.append(int(line))

possible_combinations = list(combinations(inputLines, 2))
li = [each for each in possible_combinations if sum(each) == 2020]
if li:
    print("List -> ", *li)
    print(prod(*li))
else:
    print("None found")

