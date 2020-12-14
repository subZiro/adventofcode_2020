# -*- coding: utf-8 -*-
# --- Day 3: Toboggan Trajectory --- # 

"""
Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. 
You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. 
For example in:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

"""


def get_binom():
	"""
	Получение бинома леса
	"""
	f = open('../data/day_3.txt', 'r')
	return [line[:-1] for line in f]


def count_m_rb(forest_binom: list, right_down: list):
	"""
	Возвращает количество шагов и минимальное количество повторений бинома
	"""
	count_move = len(forest_binom) // right_down[1]
	repeat_binom = len(forest_binom[0]) * count_move // len(forest_binom[0]) * right_down[0]
	return count_move, repeat_binom


def get_array_forest(forest: list, move: list, count_move: int):
	"""
	Возвращает массив ходов которыми заканчиается пересечение с деревом (#)
	"""
	result = [] 
	rd_move = [0, 0]
	for i in range(count_move):
		position = forest[rd_move[1]][rd_move[0]]
		rd_move[0] += move[0]
		rd_move[1] += move[1]
		if position == '#':
			result.append(i)
	return result


# --- Part One --- #
"""
Starting at the top-left corner of your map and following a slope of right 3 and down 1, 
how many trees would you encounter?
"""

# [шаг в право, шаг в низ]
rd = [3, 1]

arr = get_binom()
count_move, count_repeat_binom = count_m_rb(arr, rd)
# массив деревьев необходый для достижения правого нижнего угла
arr_binom = [line * count_repeat_binom for line in arr]
result = get_array_forest(arr_binom, rd, count_move)
print(f'part one result: {len(result)}')
