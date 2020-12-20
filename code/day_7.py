# -*- coding: utf-8 -*-
# --- Day 7: Handy Haversacks --- #


# --- Part One --- #
"""
In the above rules, the following options would be available to you:
    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which 
        could then hold your shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which 
        could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at 
least one shiny gold bag is 4.
"""


def get_data():
    """
    распарсивает содержимое сумок

    """
    with open('../data/day_7.txt', "r") as f:
        lines = f.readlines()

    # parent color bags
    list_color = [" ".join(line.split()[:2]) for line in lines]
    bag = {color:[] for color in list_color}
    bag_ref = {color:[] for color in list_color}

    for line in lines:
        if "no other" in line:
            continue
        words = line.split()
        bag_color = " ".join(words[:2])
        words_ref = iter(words[4:])

        while True:
            count = int(next(words_ref))
            ref_adj = next(words_ref)
            ref_color = next(words_ref)
            ref_name = f"{ref_adj} {ref_color}"
            bag[ref_name].append(bag_color)
            bag_ref[bag_color].append([ref_name, count])
            if next(words_ref).endswith('.'):
                break

    return bag, bag_ref


def color_in_bag_req(bag: dict, color: str):
    result = set(bag[color])
    for clr in bag[color]:
        result = result | color_in_bag_req(bag, clr)
    return result


def part_one(data: dict):
    """
    Вычисление уникальных цветов содержащих хотябы одну сумку shiny gold
    """ 
    return len(color_in_bag_req(data, 'shiny gold'))


bag_data, bag_ref_data = get_data()
result = part_one(bag_data)
print(f'part one result: {result}')
