"""Advent of Code 2020 day 18 part 2"""

from math import prod

def main():

    with open('day18/input.txt', 'r') as f:
        lines = f.read().splitlines()

    results = [calc3(expression) for expression in lines]

    print(sum(results))

def calc3(expression):
    while '(' in expression:
        open_paren = expression.index('(')
        closing = find_closing(expression, open_paren+1)
        result = calc3(expression[open_paren+1:closing])
        expression = expression[0:open_paren:] + expression[closing+1::]
        expression = expression[:open_paren] + str(result) + expression[open_paren:]

    adds = expression.split('*')
    mults = []
    for add_set in adds:
        elems = parse_elements(add_set)
        nums = []
        for val in elems:
            if val.isdigit():
                nums.append(int(val))
        mults.append(sum(nums))
    return prod(mults)


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
