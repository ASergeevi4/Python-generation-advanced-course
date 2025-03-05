# https://stepik.org/lesson/356380/step/7?unit=340495

# Почтовый индекс в Латверии имеет вид: 

# LetterLetterNumber_NumberLetterLetter
# где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).

# Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.

# Примечание 1. Пример правильного (неправильного) индекса Латверии:

# AB23_56VG          # правильный
# V3F_231GT          # неправильный
# Примечание 2. Обратите внимание на символ _ в почтовом индексе.

# Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.

import random 

def generate_index():
    result = ''
    result += ''.join([chr(random.randint(65,90)) for _ in range(2)])
    result += str(random.randrange(100)) + '_'
    result += str(random.randrange(100))
    result += ''.join([chr(random.randint(65,90)) for _ in range(2)])
    return  result
