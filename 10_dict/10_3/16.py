# https://stepik.org/lesson/446696/step/16?unit=437002

# Исправление дубликатов 🌶️
# На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так, чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.

# Формат входных данных
# На вход программе подается строка текста, содержащая строки-идентификаторы, разделенные символом пробела.

# Формат выходных данных
# Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.

words = input().split()
word_count = {}
result = []

for word in words:
    if word in word_count: 
        word_count[word] += 1
        new_word = f"{word}_{word_count[word] - 1}"
    else: 
        word_count[word] = 1
        new_word = word
    
    result.append(new_word)

print(" ".join(result)) 
