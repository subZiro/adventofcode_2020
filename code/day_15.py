# -*- coding: utf-8 -*-

from collections import defaultdict, deque


# --- Day 15: Rambunctious Recitation --- # 

"""
In this game, the players take turns saying numbers. 
They begin by taking turns reading from a list of starting numbers (your puzzle input). 
Then, each turn consists of considering the most recently spoken number:

    - If that was the first time the number has been spoken, the current player says 0.
    - Otherwise, the number had been spoken before; 
    the current player announces how many turns apart the number is from when it was previously spoken.
"""


def get_data(i_: int = 0, is_test: bool = True, is_part_one: bool = True):
    """получение данных"""

    test = [[0,3,6], [1,3,2], [2,1,3], [1,2,3], [2,3,1], [3,2,1], [3,1,2]]
    result_test = [[436, 1, 10, 27, 78, 438, 1836], [175594, 2578, 3544142, 261214, 6895259, 18, 362]]
    train = [[6,13,1,15,2,0], [6,13,1,15,2,0]]

    if is_part_one:
        return (test[i_], result_test[0][i_]) if is_test else (train[0], 0)
    return (test[i_], result_test[1][i_]) if is_test else (train[1], 0)


def get_result(array: list, indx: int):
    """Получение результата первой задачи"""    

    last_num = array[-1]
    turn_num = defaultdict(deque)

    for val, key in enumerate(array):
        turn_num[key].append(val + 1)

    turn = len(array)
    while turn != indx:
        turn+=1
        l = len(turn_num[last_num]) 
        if l > 1:
            last_num = turn_num[last_num][-1] - turn_num[last_num][-2]
            turn_num[last_num].append(turn)
        else:
            last_num = 0
            turn_num[last_num].append(turn)

    return last_num


# --- Test Part One --- #
indx = 2020
result_test_one = [get_result(t, indx)==r for t, r in [get_data(i, True, True) for i in range(7)]]
print(f'Test part one is {True if all(result_test_one) else False}')

# --- Part One --- #
data, _ = get_data(is_test=False, is_part_one=True)
result_one = get_result(data, indx)
print(f'Result part one: {result_one}')

# --- Test Part Two --- #
indx = 30000000
result_test_one = [get_result(t, indx)==r for t, r in [get_data(i, True, False) for i in range(7)]]
print(f'Test part two is {True if all(result_test_one) else False}')

# --- Part Two --- #
data, _ = get_data(is_test=False, is_part_one=False)
result_two = get_result(data, indx)
print(f'Result part two: {result_two}')


