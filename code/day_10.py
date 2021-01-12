# -*- coding: utf-8 -*-
# --- Day 10: Adapter Array --- # 


def get_data():
    """получение списка чисел из файла"""
    with open('../data/day_10.txt', "r") as f:
        lines = f.readlines()

    result = [int(line.strip())for line in lines]
    return sorted(result)


def get_dif_array(data, last_number=0):
    """
    получение массива разности колебаний
    """
    data_dif = []
    for n in data:
        data_dif.append(n-last_number)
        last_number = n
    data_dif.append(3)  # last +3 
    return data_dif


def part_one(data):
    """
    Получение результата первой задачи
    """
    dif_data = get_dif_array(data)
    return dif_data.count(1)*dif_data.count(3)
    

def mix_force_data(data):
    """
    """
    tmp = []
    result = []

    for x in data:
        if x == 1:
            tmp.append(x)
        else:
            if len(tmp) > 3:
                cnt_ = (len(tmp)-1) * 2 + (len(tmp)-3)
                result.append(cnt_)
            elif len(tmp) > 1:
                cnt_ = (len(tmp)-1)*2
                result.append(cnt_)
            tmp = []

    return result


def part_two(data):
    """
    Получение результата второй задачи
    """
    mix_data = mix_force_data(data)

    result = 1
    for x in mix_data:
        result = result * x
    return result


data = get_data()

# --- Part One --- #
result_one = part_one(data)
print(f'part one result: {result_one}')

# --- Part Two --- #
data_dif = get_dif_array(data)
result = part_two(data_dif)
print(f'part two result: {result}')
