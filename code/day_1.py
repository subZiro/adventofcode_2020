# -*- coding: utf-8 -*-
#--- Day 1: Report Repair ---#
#--- День 1: Отчет о ремонте ---#


from itertools import combinations
 
arr_0 = [1721, 979, 366, 299, 675, 1456]
x = 2020

f = open('../data/day_1.txt', 'r')
arr = [int(line.rstrip()) for line in f]

# --- Part One --- #
"""
В этом списке суммируются две записи 2020: 1721и 299. 
Их умножение дает 1721 * 299 = 514579 правильный ответ 514579.
"""
comb = combinations(arr, 2)
result = [c[0] * c[1] for c in comb if sum(c) == x]
print(f'Part One: {result}')


# --- Part One --- #
"""
Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. 
Multiplying them together produces the answer, 241861950.
"""
comb = combinations(arr, 3)
result = [c[0] * c[1] * c[2] for c in comb if sum(c) == x]
print(f'Part Two: {result}')



