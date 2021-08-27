# -*- coding: utf-8 -*-

import re 


# --- Day 16: Ticket Translation --- #

def get_data(file: str = '16'):
    """получение данных"""
    with open(f'../data/day_{file}.txt', "r") as f:
        lines = f.readlines()

    a = []
    b = []
    c = []
    current = True
    nearby = False
    your = False

    for line in lines:
        if current:  # корректные значения биллетов
            seq = re.findall('\d+', line)
            indx = 0
            while indx < 3 and len(seq) > 0:
                a_tmp = [numb for numb in range(int(seq[indx]),int(seq[indx +1]) + 1)]
                a.extend(a_tmp)
                a = list(set(a))
                indx += 2
            sorted(a)
        elif your and not b:  # ваш биллет
            b = [int(x) for x in line.split(',')]
        elif nearby:  #  другие биллеты
            c.extend([int(x) for x in line.split(',')])

        if len(seq) == 0:
            current = False
        if line.startswith('your'):
            your = True
        if line.startswith('nearby'):
            nearby = True
            your = False

    return a, b, c

def part_one(num_ticket: list, your_t: list, nearby_t: list):
    """Получение результата первой задачи"""

    result = sum(list(set(nearby_t) - set(num_ticket)))
    result_2 = sum(list(set(nearby_t) - set(your_t)))
    print(result)
    print(result_2)


    # rules, my_ticket, nearby_tickets = data

    # ans = 0
    # for ticket in nearby_t:
    #     for num in ticket:
    #         check = False

    #         for ranges in rules.values():
    #             for from_num, to_num in ranges:
    #                 if from_num <= num <= to_num:
    #                     check = True

    #         if not check:
    #             ans += num

    # print(ans)

    return 




# --- Test Part One --- #
result = 71
current_t, your_t, nearby_t = get_data('16_test')
result_test_one = part_one(current_t, your_t, nearby_t)
print(f'Test part one is {result == result_test_one}')

# --- Part One --- #  21956  3709435214239
current_t, your_t, nearby_t = get_data()
result_one = part_one(current_t, your_t, nearby_t)
print(f'Result part one: {result_one}')





print()
print()


def part1(data):
    rules, _, nearby_tickets = data

    ans = 0
    for ticket in nearby_tickets:
        for num in ticket:
            check = False

            for ranges in rules.values():
                for from_num, to_num in ranges:
                    if from_num <= num <= to_num:
                        check = True

            if not check:
                ans += num
    return ans



def extract_data(lines) -> (dict[list[(int, int)]], list[int], list[list[int]]):
    # rules
    # e.g.
    # {
    #     class: [(1, 2), (5, 7)]
    #     row: [(6, 11), (33, 44)]
    #     seat: [(13, 40), (45, 50)]
    # }
    ix = 0
    rules = {}
    while lines[ix]:
        name, ranges = lines[ix].split(':')
        ranges = map(str.strip, ranges.split('or'))
        int_ranges = []
        for r in ranges:
            from_num, to_num = r.split('-')
            int_ranges.append((int(from_num), int(to_num)))
        rules[name] = int_ranges
        ix += 1

    # My ticket
    # e.g. [7, 1, 14]
    ix += 2
    my_ticket = list(map(int, lines[ix].split(',')))

    # Nearby tickets
    # e.g.
    # [
    #     [7, 3, 47],
    #     [40, 4, 50],
    #     [55, 2, 20],
    #     [38, 6, 12],
    # ]
    ix += 2
    nearby_tickets = []
    for line in lines[ix+1:]:
        nearby_tickets.append(list(map(int, line.split(','))))

    return rules, my_ticket, nearby_tickets


with open('../data/day_16.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]

    print(part1(extract_data(inputs)))



print()



from collections import defaultdict
import math
import re

tickets = []
ticket_fields = dict()
ticket_positions = defaultdict(list)
invalid_values = list()

sections = open('../data/day_16.txt').read().split('\n\n')

# Parse in first section into ticket fields dictionary.
for line in sections[0].split('\n'):
    key, s1, e1, s2, e2 = re.split(' or |-|: ', line)
    ticket_fields[key] = set.union(set(range(int(s1), int(e1) + 1)), set(range(int(s2), int(e2) + 1)))

# Parse in my ticket information
my_ticket = list(map(int, sections[1].split('\n')[1].split(',')))

# For part 1, a ticket is invalid if its number does not fit in the union of all sets of ranges.
all_valid_numbers = set.union(*ticket_fields.values())

# Parse in valid tickets, and store invalid numbers
for line in sections[2].split('\n')[1:-1]:
    ticket_numbers = list(map(int, line.split(',')))
    invalid_ticket_values = [num for num in ticket_numbers if num not in all_valid_numbers]
    if len(invalid_ticket_values) > 0:
        invalid_values.extend(invalid_ticket_values)
        continue
    tickets.append(ticket_numbers)

# Make a list of all the candidate fields each ticket position could be.
for i in range(len(my_ticket)):
    for key, val in ticket_fields.items():
        if all([ticket[i] in val for ticket in tickets]):
            ticket_positions[i].append(key)

# Find all the fields that are unique (i.e. have length of 1). These fields *must* be the correct position,
# so remove it from any other list of candidate ticket positions.
uniques = [pos[0] for pos in ticket_positions.values() if len(pos) == 1]

# Repeat this process until all ticket positions as unique.
while len(uniques) != len(ticket_positions):
    for unique in uniques:
        for val in ticket_positions.values():
            if len(val) > 1 and unique in val:
                val.remove(unique)
    uniques = [pos[0] for pos in ticket_positions.values() if len(pos) == 1]

# Get the departure value positions and pull from my ticket information
departure_values = [my_ticket[k] for k, v in ticket_positions.items() if 'departure' in v[0]]

# Part 1 is the sum of all the invalid numbers, Part 2 is the product of the departure values.
print(f"Part 1 Answer: {sum(invalid_values)}")
print(f"Part 2 Answer: {math.prod(departure_values)}")
