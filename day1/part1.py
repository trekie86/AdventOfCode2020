inputLines = []
with open("./part1input.txt", "r") as f:
    inputLines = f.read().splitlines()

for x in range(len(inputLines)):
    for y in range(x + 1, len(inputLines)):
        # print(f"Combo [{x}, {y}]")
        print(f"Checking positions {x} & {y} with values {inputLines[x]} & {inputLines[y]}")
        if( (int(inputLines[x]) + int(inputLines[y])) == 2020):
            print(f"Match found: {inputLines[x]} & {inputLines[y]}")
            print(f"Resulting value: {int(inputLines[x]) * int(inputLines[y])}")
            break;
    else:
        continue
    break;

