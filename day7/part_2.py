"""Advent of Code 2020 Day 7 part 1"""

import re

def main():
    """The main method"""
    with open('day7/input.txt', 'r') as f:
        lines = f.read().splitlines()

    bag_map = build_tree(lines)
    count = 0
    count += recurse_bag_count(bag_map, 'shiny gold')

    print(count)

def recurse_bag_count(bag_map, current_bag):
    """Count how many bags exist recursively in the bag being requested"""
    result = 0
    if bag_map.get(current_bag):
        current_bags = bag_map[current_bag]
        for bag_color, count in current_bags.items():
            result += count + count*recurse_bag_count(bag_map, bag_color)
        return result
    else:
        return 0

def build_tree(lines: []) -> {}:
    """Builds a tree-ish structure that is the key from a bag type
    to a map of bag types and their value of quantity"""
    key_regex = re.compile(r"(?P<key_val>^.*) bags contain(?P<contents>.*$)")
    values_regex = re.compile(r"(?P<count>\d) (?P<color>.+?(?= bag))")
    bag_map = {}
    for line in lines:
        match = key_regex.match(line)
        key = match['key_val']
        bag_map[key] = {}
        contents = match['contents']
        content_matches = values_regex.findall(contents)
        for color_match in content_matches:
            bag_map[key][color_match[1]] = int(color_match[0])

    return bag_map

if __name__ == "__main__":
    # execute only if run as a script
    main()
