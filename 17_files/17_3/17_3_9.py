# https://stepik.org/lesson/530408/step/9?unit=523223

# Длинные строки ↔️
# Вам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу, которая выводит все строки наибольшей длины из файла, не меняя их порядок.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести строки указанного файла, имеющие наибольшую длину, не меняя их порядка.

# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

# Примечание 2. Используйте менеджер контекста. 🙂

# with open('lines.txt', 'rt', encoding='utf-8') as file:
#     longest = len(file.readline())
#     result = []
#     file.seek(0)
#     for line in file:
#         if len(line) > longest:
#             longest = len(line)
#             result.clear()
#             result.append(line)
#         elif len(line) == longest:
#             result.append(line)
#     print(*[el.strip() for el in result], sep='\n')

with open('lines.txt', 'rt', encoding='utf-8') as file:
    max_len = max(len(line.strip()) for line in file.readlines())
    file.seek(0)
    print(*[line.strip() for line in file.readlines() if len(line.strip()) == max_len], sep='\n')
