# -*- coding: utf-8 -*-
# --- Day 10: Adapter Array --- # 


def get_data():
    """получение списка чисел из файла"""
    with open('../data/day_10.txt', "r") as f:
        lines = f.readlines()

    result = [int(line.strip())for line in lines]
    return sorted(result)


# --- Part One --- #
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
    

data = get_data()
result_one = part_one(data)
print(f'part one result: {result_one}')

