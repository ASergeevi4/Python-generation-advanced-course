# https://stepik.org/lesson/356380/step/8?unit=340495

# Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы (двумерного списка).

# Примечание. Выводить содержимое матрицы не нужно.

# from random import shuffle as sh

# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]

# for el in matrix:
#     sh(el)

import random as rnd

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

lst = sum(matrix, [])
rnd.shuffle(lst)
new_matrix = []
m = len(matrix[0])

for i in range(0, len(lst), m):
    new_matrix.append(lst[i:i + m])

matrix = new_matrix
