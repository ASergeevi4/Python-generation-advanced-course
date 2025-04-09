# https://stepik.org/lesson/530408/step/13?unit=523223

# Random name and surname 🎲
# Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.

# Напишите программу, которая c помощью модуля random создает 3 случайные пары имя + фамилия, а затем выводит их, каждую на отдельной строке.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести текст в формате, приведенном в примере.

import random

with open('first_names.txt', encoding='utf-8') as name, open('last_names.txt', encoding='utf-8') as surname:
    list_of_names = [line.strip() for line in name]
    list_of_surnames = [line.strip() for line in surname]
    for _ in range(3):
        print(random.choice(list_of_names), random.choice(list_of_surnames))
