"""Advent of Code 2020 day 18 part 1"""

def main():

    with open('day18/input.txt', 'r') as f:
        lines = f.read().splitlines()

    results = [calc2(expression) for expression in lines]

    print(sum(results))

def calc2(expression):
    elems = parse_elements(expression)
    pos = 0
    nums = []
    ops = []
    while pos < len(elems):
        if elems[pos].isdigit():
            nums.append(int(elems[pos]))
            pos += 1
            # numbers to crunch
        elif elems[pos] in '+*':
            ops.append(elems[pos])
            pos += 1
        elif elems[pos] == '(':
            end = find_closing(elems, pos+1)
            nums.append(calc2(elems[pos+1:end]))
            pos = end+1
    result = nums.pop(0)
    while len(nums) > 0:
        op = ops.pop(0)
        if op == '+':
            result = add(result, nums.pop(0))
        elif op == '*':
            result = multiply(result, nums.pop(0))
    return result


def find_closing(elems, start):
    depth = 0
    for i in range(start, len(elems)):
        if elems[i] == ')':
            if depth == 0:
                return i
            else:
                depth -= 1
        elif elems[i] == '(':
            depth += 1


def parse_elements(expression):
    elements = [''] #Empty starting element
    for char in expression:
        if char.isdigit():
            if elements[-1].isdigit():
                elements[-1] += char
            else:
                elements.append(char)
        elif char in '+-*/()':
            elements.append(char)
    return elements[1:]



def add(x,y):
    return x + y

def multiply(x,y):
    return x * y

if __name__ == '__main__':
    main()
