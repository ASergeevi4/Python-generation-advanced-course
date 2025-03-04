# https://stepik.org/lesson/446698/step/12?unit=437004

# Дополните приведенный код, используя генератор, так, чтобы получить словарь result , в котором ключом будет строка – элемент списка words, а значением – список соответствующих кодов ASCII символов данной строки.

# Примечание 1. Если бы список words имел вид: words = ['yes', 'hello'], то результатом был бы словарь

# result = {'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111]}

# Примечание 2. Для получения ASCII кода символа используйте функцию ord().

# Примечание 3. Выводить содержимое словаря result не нужно.

words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {word: [ord(c) for c in word] for word in words}

# simplier and much clear option:

# ______________

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

# result = {}
# for el in words:
#     result[el] = [ord(i) for i in el]
