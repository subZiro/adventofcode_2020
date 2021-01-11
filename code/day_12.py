# -*- coding: utf-8 -*-


# --- Day 12: Rain Risk --- # 

"""
The navigation instructions (your puzzle input) consists of a sequence of single-character 
actions paired with integer input values. After staring at them for a few minutes, 
you work out what they probably mean:
    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.
"""


def get_data():
    """получение списка чисел из файла"""

    with open('../data/day_12.txt', "r") as f:
        lines = f.readlines()
    result = [(line.strip()[0], int(line.strip()[1:])) for line in lines]

    return result

def move(pos, dir, mv):
    """Движение корабля"""
 
    if dir == 'F':
        pos[1][pos[0]] += mv
    elif dir == 'R':
        for i in range(mv // 90):
            if pos[0] == 'N':
                pos[0] = 'E'
            elif pos[0] == 'S':
                pos[0] = 'W'
            elif pos[0] == 'E':
                pos[0] = 'S'
            elif pos[0] == 'W':
                pos[0] = 'N'
    elif dir == 'L':
        for i in range(mv // 90):
            if pos[0] == 'N':
                pos[0] = 'W'
            elif pos[0] == 'S':
                pos[0] = 'E'
            elif pos[0] == 'E':
                pos[0] = 'N'
            elif pos[0] == 'W':
                pos[0] = 'S'
    else:
        pos[1][dir] += mv

    return pos


# --- Part One --- #
def part_one(data: list, start: str = 'E'):
    """Получение результата первой задачи"""

    position = [start, {'N': 0, 'S': 0, 'E': 0, 'W': 0}]  # направление коробля, (N, S, E, W)
    for d, m in data:
        position = move(position, d, m)

    result = abs(position[1]['N'] - position[1]['S']) + abs(position[1]['E'] - position[1]['W'])
    return result


data = get_data()
result_one = part_one(data)
print(f'part one result: {result_one}')



# --- Part Two --- #

import math


def rotate(origin, point, angle):
    # source: https://stackoverflow.com/a/34374437
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))


def part_two(data: list):
    """Получение результата первой задачи"""

    position = {'x': 0, 'y': 0}  # координаты коробля
    point = {'x': 10, 'y': 1}  # координаты точки

    for dr, mv in data:
        if dr == 'N':
            point['y'] += mv
        elif dr == 'S':
            point['y'] -= mv
        elif dr == 'E':
            point['x'] += mv
        elif dr == 'W':
            point['x'] -= mv
        elif dr == 'F':
            position['x'] += point['x'] * mv
            position['y'] += point['y'] * mv
        elif dr in ['L', 'R']:
            if dr == 'R':
                mv = -mv
            point['x'], point['y'] = rotate((0, 0), (point['x'], point['y']), math.radians(mv))

    return abs(position['x']) + abs(position['y'])


result_two = part_two(data)
print(f'part two result: {result_two}') 


