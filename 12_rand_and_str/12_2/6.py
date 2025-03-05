# https://stepik.org/lesson/356380/step/6?unit=340495

# IP-адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных точкой.

# Напишите функцию generate_ip(), которая с помощью модуля random генерирует и возвращает случайный корректный IP-адрес.

import random

def generate_ip():
    list_of_nums = []
    for _ in range(4):
        list_of_nums.append(random.randint(0,255))
    return '.'.join(str(i) for i in list_of_nums)
