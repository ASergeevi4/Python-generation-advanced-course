# https://stepik.org/lesson/356380/step/13?unit=340495

# Генератор паролей 1
# Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой: «l» (L маленькое); «I» (i большое); «1» (цифра); «o» и «O» (маленькая и большая буквы); «0» (цифра).

# Формат входных данных
# На вход программе подаются два числа n и m, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести n паролей длиной m символов в соответствии с условием задачи, каждый на отдельной строке.

# Примечание 1. Считать, что числа n и m всегда таковы, что требуемые пароли сгенерировать возможно.

# Примечание 2. В каждом пароле необязательно должна присутствовать хотя бы одна цифра и буква в верхнем и нижнем регистре.

# Примечание 3. Решение задачи удобно оформить в виде двух вспомогательных функций:

# функция generate_password(length) – возвращает случайный пароль длиной length символов;
# функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length символов.
# Примечание 4. Приведенные ниже тесты – это лишь образцы возможного ответа. Возможны и другие способы генерации паролей.

import random
import string

n, m = int(input()), int(input())

def make_password(pass_length: int) -> str:
    prohibited_symbols = 'lI1oO0'
    good_symbols = f'{string.ascii_letters}' + f'{string.digits}'
    result = ''.join(el for el in good_symbols if el not in prohibited_symbols)
    password = ''.join(random.sample(result,pass_length))
    return password

def generate_passwords(count: int, length:  int) -> list:
    result = []
    for _ in range(count):
         result.append(make_password(length))
    return result

print(*generate_passwords(n,m), sep='\n')
