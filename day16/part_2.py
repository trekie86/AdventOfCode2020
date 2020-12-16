"""Advent of Code 2020 day 16 part 2"""

import itertools
from math import prod

def main():
    with open('day16/input.txt', 'r') as f:
        lines = f.read().splitlines()

    idx_list = [idx + 1 for idx,val in enumerate(lines) if val == '']
    size = len(lines)
    res = [lines[i: j] for i,j in zip([0] + idx_list, idx_list + ([size] if idx_list[-1] != size else []))]

    conditions = res[0][:-1]
    my_ticket = res[1][1:-1][0].split(',')
    nearby_tickets = res[2][1:]
    print(f"Total tickets {len(nearby_tickets)}")
    condition_map = build_condition_map(conditions)
    invalid_tickets = []
    for ticket in nearby_tickets:
        valid = evaluate_ticket(condition_map,[int(x) for x in ticket.split(',')])
        if not valid:
            invalid_tickets.append(ticket)
    valid_tickets = [x.split(',') for x in nearby_tickets if x not in invalid_tickets]

    print(f"Valid ticket count {len(valid_tickets)}")

    ticket_param_possible = []
    for i in range(len(valid_tickets[0])):
        ticket_param_possible.append(list(condition_map.keys()).copy())
    # print(ticket_param_possible)
    for i in range(len(ticket_param_possible)):
        evaluate_ticket_single_val(condition_map, valid_tickets, i, ticket_param_possible)

    defined_params = {}
    defined = 0
    while defined < len(ticket_param_possible):
        for idx,val in enumerate(ticket_param_possible):
            if len(val) == 1:
                value = val[0]
                defined_params[value] = idx
                defined += 1
                for param in ticket_param_possible:
                    if value in param:
                        param.remove(value)

    print(defined_params)
    concerned_values = []
    for k,v in defined_params.items():
        if k.startswith('departure'):
            concerned_values.append(int(my_ticket[v]))
    print(prod(concerned_values))

def build_condition_map(conditions):
    condition_map = {}
    for condition in conditions:
        condition_split = condition.split(': ')
        split_condition = condition_split[1].split(' or ')
        first_condition = split_condition[0]
        second_condition = split_condition[1]
        first_condition_split = first_condition.split('-')
        second_condition_split = second_condition.split('-')
        condition_map[condition_split[0]] = [range(int(first_condition_split[0]), int(first_condition_split[1])+1), range(int(second_condition_split[0]), int(second_condition_split[1])+1)]

    return condition_map

def evaluate_ticket_single_val(condition_map, tickets, idx, ticket_param_possible):
    for k,v in condition_map.items():
        for ticket in tickets:
            if not condition_check(int(ticket[idx]), v[0], v[1]):
                if k in ticket_param_possible[idx]:
                    ticket_param_possible[idx].remove(k)
                    break

def condition_check(val, cond1, cond2):
    return val in cond1 or val in cond2

def evaluate_ticket(condition_map, ticket_values):
    for ticket in ticket_values:
        condition_met = False
        for condition in itertools.chain.from_iterable(condition_map.values()):
            if ticket in condition:
                condition_met = True
                break
        if not condition_met:
            return False
    return True



if __name__ == '__main__':
    main()
