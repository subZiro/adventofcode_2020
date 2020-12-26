# -*- coding: utf-8 -*-
# --- Day 9: Encoding Error --- #

from itertools import combinations


# --- Part One --- #
"""
For example, suppose your preamble consists of the numbers 1 through 25 in a random order. 
To be valid, the next number must be the sum of two of those numbers:
    26 would be a valid next number, as it could be 1 plus 25 (or many other pairs, like 2 and 24).
    49 would be a valid next number, as it is the sum of 24 and 25.
    100 would not be valid; no two of the previous 25 numbers sum to 100.
    50 would also not be valid; although 25 appears in the previous 25 numbers, 
        the two numbers in the pair must be different.

Suppose the 26th number is 45, and the first number 
(no longer an option, as it is more than 25 numbers ago) was 20. 
Now, for the next number to be valid, there needs to be some pair of numbers among 1-19, 
21-25, or 45 that add up to it:
    26 would still be a valid next number, as 1 and 25 are still within the previous 25 numbers.
    65 would not be valid, as no two of the available numbers sum to it.
    64 and 66 would both be valid, as they are the result of 19+45 and 21+45 respectively.
"""

def get_data():
    """получение списка чисел из файла"""
    with open('../data/day_9.txt', "r") as f:
        lines = f.readlines()

    result = [int(line.strip())for line in lines]
    return result


def part_one(data: list, pre: int):
    """ 
    получение первого числа не соответствующего eXchange-Masking Addition System алгоритму шифрования 
    """
    for i in range(pre, len(data)):
        comb = combinations(data[i-pre:i], 2)
        sum_in_comb = [sum(x)==data[i] for x in comb]
        if not any(sum_in_comb):
            return data[i]
    return None


data = get_data()
result = part_one(data, 25)
print(f'part one result: {result}')


# --- Part Two --- #
"""
The final step in breaking the XMAS encryption relies on the invalid number you just found: 
you must find a contiguous set of at least two numbers in your list which sum to the invalid 
number from step 1.
"""


def get_min_max_sum(data: list):
    """
    Возвращает сумму минимального и максимального элемента списка data
    """
    return min(data) + max(data)


def part_two(data: list, num: int):
    """
    Возвращает результат второго задания
    """
    arr = []
    for x in data:
        arr.append(x)
        if sum(arr) > num:
            while not sum(arr) <= num:
                del arr[0]
        if sum(arr) == num:
            return get_min_max_sum(arr)
    return None


result_two = part_two(data, result)
print(f'part two result: {result_two}')


