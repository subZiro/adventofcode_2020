# -*- coding: utf-8 -*-
# --- Day 11: Seating System --- # 

from copy import deepcopy


def get_data():
    """получение списка чисел из файла"""
    with open('../data/day_11.txt', "r") as f:
        lines = f.readlines()
    result = [[x for x in line.strip()] for line in lines]

    return result


def seating(data, data_cp, limit):
	"""
	Рассадка на места по условию
	"""
	is_edited = False
	for i, y in enumerate(data):
		for j, x in enumerate(y):
			cr = count_recirved(i, j, data, limit==5)

			if data[i][j] == 'L' and cr == 0:
				data_cp[i][j] = '#'
				is_edited = True
			elif data[i][j] == '#' and cr >= limit:
				data_cp[i][j] = 'L'
				is_edited = True

	return is_edited, data_cp


def while_seating(data, limit):
	"""
	повторение рассадки пока не количество занятых мест меняется
	"""

	while True:
		new_data = deepcopy(data)
		flg, data = seating(data, new_data, limit)
		if not flg:
			return count_recerve(data)
		data = deepcopy(data)


def count_recirved(a, b, data, is_two):
	"""
	Подсчитывает количество занятых рядом мест
	"""

	count = 0
	for y in [-1, 0, 1]:
		for x in [-1, 0, 1]:
			if not (y == 0 and x == 0):
				ay = a + y
				bx = b + x
				if is_two:
					while 0 <= ay < len(data) and 0 <= bx < len(data[a]) and data[ay][bx] == '.':
						ay = ay + y
						bx = bx + x
				if 0 <= ay < len(data) and 0 <= bx < len(data[a]) and data[ay][bx] == '#':
					count += 1 
	return count


def count_recerve(seating_array):
	"""
	возвращает количество занятых мест
	"""

	arr = [s for line in seating_array for s in line if s == '#']
	return len(arr)


def part_one(data):
	"""
	Получение результата первой задачи
	"""
	return while_seating(data, 4)


def part_two(data: list):
	"""
	Получение результата первой задачи
	"""
	return while_seating(data, 5)


data = get_data()

# --- Part One --- #
result_one = part_one(data)
print(f'part one result: {result_one}')

# --- Part Two --- #
result_two = part_two(data)
print(f'part two result: {result_two}')

