# -*- coding: utf-8 -*-
# --- Day 14: Docking Data --- #


from itertools import product


def get_data():
    """получение данных"""

    with open('../data/day_14.txt', "r") as f:
        lines = f.readlines()
    return lines


def update_memory(memory: dict, command: list, mask: str):
    """Обновление значения в памяти"""

    val = int(command[1])
    for i, v in enumerate(mask):
        if v == 'X':
            pass
        elif v == '1':
            val = val | (2 ** (36 - i - 1))
        elif v == '0':
            val = val & ~(2 ** (36 - i - 1))
    memory[command[0]] = val
    return memory         


def get_product_masks(mask):
    """
    Получение возможных вариаций масок
    """

    masks = []

    mask_bits = [i for i, v in enumerate(mask) if v == 'X']
    mask_product = [''.join(x) for x in product('21', repeat=len(mask_bits))]

    new_mask = mask[:]
    for mask_prdc in mask_product:
        bit_vals = dict(zip(mask_bits, mask_prdc))
        for val in bit_vals:
            new_mask = new_mask[:val] + bit_vals[val] + new_mask[val+1:]
        masks.append(new_mask)
    return masks


def update_memory_two(memory: dict, command: list, mask: str):
    """Обновление значения в памяти для 2 задачи"""
    
    target_addr = int(command[0][4:-1])
    target_value = int(command[1])

    addrs = []
    masks = get_product_masks(mask)
    for mask in masks:
        for i, v in enumerate(mask):
            if v == '1':
                target_addr = target_addr | (2 ** (36 - i - 1))
            elif v == '2':
                target_addr = target_addr & ~(2 ** (36 - i - 1))
        addrs.append(target_addr)

    for addr in addrs:
        memory[addr] = target_value
    return memory


def get_result(lines: list, func, part_one: bool):
    """Получение результата задачи"""

    memory = {}
    mask = ''

    for line in lines:
        if line.startswith('mask'):
            mask = line[7:]
        else:
            command = line.replace(' = ', ' ').split()
            if part_one:
                memory[command[0]] = command[1]
            memory = func(memory, command, mask)

    return sum([memory[key] for key in memory]) 


data = get_data()

# --- Part One --- #
result_one = get_result(data, update_memory, True)
print(f'part one result: {result_one}')

# --- Part Two --- #
result_two = get_result(data, update_memory_two, False)
print(f'part two result: {result_two}')

