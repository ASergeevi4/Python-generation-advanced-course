# https://stepik.org/lesson/488831/step/4?unit=480067

# Словарь синонимов
# Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу, которая для одного данного слова определяет его синоним.

# Формат входных данных
# На вход программе подается количество пар синонимов n. Далее следует n строк, каждая строка содержит два слова-синонима. После этого следует одно слово, синоним которого надо найти.

# Формат выходных данных
# Программа должна вывести одно слово, синоним введенного.

# Примечание 1. Гарантируется, что синоним введенного слова существует в словаре.

# Примечание 2. Все слова в словаре начинаются с заглавной буквы.

my_dict = {}

for _ in range(int(input())):
    key, value = input().split()
    my_dict[key] = value
    my_dict[value] = key
reqst = input()
print(my_dict)
