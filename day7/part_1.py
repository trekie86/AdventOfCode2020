"""Advent of Code 2020 Day 7 part 1"""

from collections import defaultdict
import re

def main():
    """The main method"""
    with open('day7/input.txt', 'r') as f:
        lines = f.read().splitlines()

    bag_map = build_tree(lines)
    inverted_map = invert_map(bag_map)
    # print(bag_map)
    # print(inverted_map)

    containing_set = set([])
    queue = []

    containing_set.update(inverted_map['shiny gold'])
    for bag in inverted_map['shiny gold']:
        queue.append(bag)

    while len(queue) > 0:
        key = queue.pop()
        bags = inverted_map.get(key)
        if bags:
            for bag in bags:
                containing_set.add(bag)
                queue.append(bag)

    print(containing_set)
    print(len(containing_set))

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
        # bag_map[key][]
        content_matches = values_regex.findall(contents)
        for color_match in content_matches:
            bag_map[key][color_match[1]] = int(color_match[0])

    return bag_map

def invert_map(bag_map: {}) -> {}:
    """Invert the map where the key is the bag that can be contained in other bags"""
    inverted_map = defaultdict(list)
    for key, val in bag_map.items():
        for sub_key in val.keys():
            inverted_map[sub_key].append(key)

    return inverted_map

if __name__ == "__main__":
    # execute only if run as a script
    main()
