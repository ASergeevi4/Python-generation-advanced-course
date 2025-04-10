# https://stepik.org/lesson/511854/step/12?unit=504046

# Интересные числа
# На вход программе подаются два натуральных числа a и b. Напишите программу с использованием встроенной функции all() для обнаружения всех целых чисел в диапазоне [a;b], которые делятся на каждую содержащуюся в них цифру без остатка.

# Формат входных данных
# На вход программе подаются два натуральных числа a и b на отдельных строках.

# Формат выходных данных
# Программа должна вывести все числа из диапазона [a;b], удовлетворяющие условию задачи, на одной строке, разделяя их символом пробела.

# Примечание. Числа, содержащие нули, неинтересны, их выводить не нужно.

for num in range(int(input()), int(input()) + 1):
    digits = list(map(int, str(num)))
    if all(x != 0 and num % x == 0 for x in digits):
        print(num, end=' ')
