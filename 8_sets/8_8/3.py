# https://stepik.org/lesson/445793/step/3?unit=436054

# Используя генератор множеств, дополните приведенный ниже код так, чтобы получить множество, содержащее уникальные значения списка items. Результат вывести на одной строке, в упорядоченном виде, разделяя элементы одним символом пробела.

# Примечание 1. Обратите внимание, некоторые элементы списка – числа, а некоторые – строки, при этом строки необходимо трактовать как числа.

items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]

print(*sorted(set(int(i) for i in items)))
