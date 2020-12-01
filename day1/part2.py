inputLines = []
with open("./part1input.txt", "r") as f:
    inputLines = f.read().splitlines()

for x in range(len(inputLines)):
    for y in range(x + 1, len(inputLines)):
        for z in range(y + 1, len(inputLines)):
            # print(f"Combo [{x}, {y}]")
            print(f"Checking positions {x} & {y} & {z} with values {inputLines[x]} & {inputLines[y]} & {inputLines[z]}")
            if( (int(inputLines[x]) + int(inputLines[y]) + int(inputLines[z])) == 2020):
                print(f"Match found: {inputLines[x]} & {inputLines[y]} & {inputLines[z]}")
                print(f"Resulting value: {int(inputLines[x]) * int(inputLines[y]) * int(inputLines[z])}")
                break;
        else:
            continue
        break
    else:
        continue
    break

