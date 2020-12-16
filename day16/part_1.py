"""Advent of Code 2020 day 16 part 1"""

def main():
    with open('day16/input.txt', 'r') as f:
        lines = f.read().splitlines()

    idx_list = [idx + 1 for idx,val in enumerate(lines) if val == '']
    size = len(lines)
    res = [lines[i: j] for i,j in zip([0] + idx_list, idx_list + ([size] if idx_list[-1] != size else []))]

    conditions = res[0][:-1]
    my_ticket = res[1][1:-1]
    nearby_tickets = res[2][1:]

    condition_list = build_condition_list(conditions)
    error_values = []
    for ticket in nearby_tickets:
        error_values.extend(evaluate_ticket(condition_list,[int(x) for x in ticket.split(',')]))

    print(sum(error_values))


def build_condition_list(conditions):
    condition_list = set([])
    for condition in conditions:
        split_condition = condition.split(': ')[1].split(' or ')
        first_condition = split_condition[0]
        second_condition = split_condition[1]
        first_condition_split = first_condition.split('-')
        second_condition_split = second_condition.split('-')
        condition_list.add(range(int(first_condition_split[0]), int(first_condition_split[1])+1))
        condition_list.add(range(int(second_condition_split[0]), int(second_condition_split[1])+1))

    return condition_list


def evaluate_ticket(condition_list, ticket_values):
    error_vals = []
    for ticket in ticket_values:
        condition_met = False
        for condition in condition_list:
            if ticket in condition:
                condition_met = True
                break
        if not condition_met:
            error_vals.append(ticket)
    return error_vals



if __name__ == '__main__':
    main()