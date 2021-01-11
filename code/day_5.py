# -*- coding: utf-8 -*-

from math import ceil, floor


# --- Day 5: Binary Boarding --- # 
# --- Part One --- #
"""
ROW For example, consider just the first seven characters of FBFBBFFRLR:
	Start by considering the whole range, rows 0 through 127.
	F means to take the lower half, keeping rows 0 through 63.
	B means to take the upper half, keeping rows 32 through 63.
	F means to take the lower half, keeping rows 32 through 47.
	B means to take the upper half, keeping rows 40 through 47.
	B keeps rows 44 through 47.
	F keeps rows 44 through 45.
	The final F keeps the lower of the two, row 44.

COL For example, consider just the last 3 characters of FBFBBFFRLR:
	Start by considering the whole range, columns 0 through 7.
	R means to take the upper half, keeping columns 4 through 7.
	L means to take the lower half, keeping columns 4 through 5.
	The final R keeps the upper of the two, column 5.

44 * 8 + 5 = 357
"""


def get_row(seat: str):
	"""получение ряда по талону seat"""
	upper = 127
	lower = 0
	for character in seat[:7]:
		if character == "F":
			upper = floor((lower + upper) / 2)
		elif character == "B":
			lower = ceil((lower + upper) / 2)
	return upper


def get_column(seat: str):
	"""получение столбца по талону seat"""
	right = 7
	left = 0
	for character in seat[-3:]:
		if character == "R":
			left = ceil((right + left) / 2)
		elif character == "L":
			right = floor((right + left) / 2)
	return right


def get_data():
	"""
	Получение списка мест
	"""
	k = 0
	result = []
	f = open('../data/day_5.txt', 'r')
	for line in f:
		k += 1
		line = line.rstrip()
		r = get_row(line)
		c = get_column(line)
		result.append(r * 8 + c)
	return result


seats_list = get_data()
print(f'max place: {max(seats_list)}')


# --- Part Two --- #
"""What is the ID of your seat?"""

your_seat = set(range(min(seats_list), max(seats_list))).difference(set(seats_list))
print(f'your seat: {your_seat.pop()}')


