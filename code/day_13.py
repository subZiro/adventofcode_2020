# -*- coding: utf-8 -*-

# --- Day 13: Shuttle Search --- # 


def get_data():
    """получение данных"""

    with open('../data/day_13.txt', "r") as f:
        lines = f.readlines()
    data = [line.rstrip('\n') for line in lines]
    time_start = int(data[0])
    buses = [int(x) if x.isdigit() else x for x in data[1].split(",")]

    return time_start, buses


def part_one(time_start: int, bus_list: list, t_delta: int = 60):
    """Получение результата первой задачи"""

    valid_time = time_start
    diff = time_start
    bus_id = time_start

    for t in range(time_start - t_delta, time_start + t_delta):
        for bus in buses:
            if bus != 'x' and t % bus == 0:
                d = abs(t - time_start)
                if t > time_start and d < diff:
                    valid_time = t
                    diff = d
                    bus_id = bus

    return bus_id * (valid_time - time_start)


def part_two(data: list):
    """Получение результата первой задачи"""

    bus_tm = {}
    for i, bus in enumerate(buses):
        if bus != 'x':
            bus_tm[bus] = -i % bus

    i = 0
    inc = 1
    for bus in bus_tm.keys():
        while True:
            i += inc
            if i % bus == bus_tm[bus]:
                break
        inc *= bus
    return i


time_start, buses = get_data()

# --- Part One --- #
result_one = part_one(time_start, buses)
print(f'part one result: {result_one}')

# --- Part Two --- #
result_two = part_two(buses)
print(f'part two result: {result_two}') 
