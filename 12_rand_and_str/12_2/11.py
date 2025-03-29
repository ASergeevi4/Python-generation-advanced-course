# https://stepik.org/lesson/356380/step/11?unit=340495

# Для игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные) целые числа от 1 до 75 (включительно), при этом центральная клетка является пустой (она заполняется числом 0).

import random


rndm_num = random.sample(list(range(1,76)), 25)
bingo = [rndm_num[i:i+5] for i in range(0,25,5)]
bingo[2][2] = 0

for row in bingo:
    for el in row:
        print(str(el).ljust(3), end=' ')
    print()
