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


time_start, buses = get_data()

# --- Part One --- #
result_one = part_one(time_start, buses)
print(f'part one result: {result_one}')
