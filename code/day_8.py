# -*- coding: utf-8 -*-
# --- Day 8: Handheld Halting --- #


# --- Part One --- #
"""
The boot code is represented as a text file with one instruction per line of text. 
Each instruction consists of an operation (acc, jmp, or nop) and an argument 
(a signed number like +4 or -20).

acc increases or decreases a single global value called the accumulator by the 
value given in the argument. For example, acc +7 would increase the accumulator by 7. 
The accumulator starts at 0. After an acc instruction, the instruction immediately 
below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to 
execute is found using the argument as an offset from the jmp instruction; for example, 
jmp +2 would skip the next instruction, jmp +1 would continue to the instruction 
immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
"""


def get_data():
    """
    распарсивает загрузочную инструкци в список списков
    """

    with open('../data/day_8.txt', "r") as f:
        lines = f.readlines()

    result = []
    for line in lines:
        inst_one = line.strip().split()
        inst_one[1] = int(inst_one[1])
       
        result.append(inst_one)
    return result

def part_one(data: list):
    """
    возвращает сумму acc перед зацикливанием инструкции программы
    """

    acc_summ = 0
    i = 0
    i_list = []
    ext_code = 0
    while True:
        if i == len(data):
            break
        if i in i_list:
            ext_code = 1
            break

        i_list.append(i)
        k, val = data[i]

        if k == 'acc':
            acc_summ += val
            i += 1
        elif k == 'jmp':
            i += val
        elif k == 'nop':
            i += 1
       
    return ext_code, acc_summ


instructions = get_data()
_, result = part_one(instructions)
print(f'part one result: {result}')
