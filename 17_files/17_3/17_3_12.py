# https://stepik.org/lesson/530408/step/12?unit=523223

# Статистика по файлу 📊
# Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести три найденных числа в формате, приведенном в примере.

# with open('file.txt', 'w', encoding='utf-8') as file:
#     file.write('''Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.''')

with open('file.txt', encoding='utf-8') as file:
    count_words = 0
    count_lines = 0
    count_symb = 0
    for line in file:
        count_words += len(line.split())
        count_lines += 1
        for symb in line:
            if symb.isalpha():
                count_symb += 1
    print(f'Input file contains:\n{count_symb} letters\n{count_words} words\n{count_lines} lines')
