# https://stepik.org/lesson/356380/step/14?unit=340495

# Генератор паролей 2 🌶️
# Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой: «l» (L маленькое); «I» (i большое); «1» (цифра); «o» и «O» (большая и маленькая буквы); «0» (цифра).

# Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.

# Формат входных данных
# На вход программе подаются два числа n и m, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести n паролей длиной m символов в соответствии с условием задачи, каждый на отдельной строке.


import random
import string

n, m = int(input()), int(input())

def make_password(pass_length: int) -> str:
    prohibited_symbols = 'lI1oO0'
    good_symbols = list((set(string.ascii_letters) | set(string.digits)) - set(prohibited_symbols))
    while True:
        rndm_pass = ''.join(random.sample(good_symbols, pass_length))
        lwr_case = any(el.islower() for el in rndm_pass)
        upr_case = any(el.isupper() for el in rndm_pass)
        digit = any(el.isdigit() for el in rndm_pass)
        if lwr_case and upr_case and digit:
            return rndm_pass
            
def generate_passwords(count: int, length:  int) -> list:             
    return [make_password(length) for _ in range(count)]

print(*generate_passwords(n,m), sep='\n')