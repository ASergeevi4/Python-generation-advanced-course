# https://stepik.org/lesson/512854/step/5?unit=505068

# Напишите функцию func, используя синтаксис анонимных функций, которая принимает целочисленный аргумент и возвращает значение True, если он делится без остатка на 19 или на 13, или False в противном случае.

func = lambda x: x % 19 == 0 or x % 13 == 0

print(func(19))
print(func(13))
print(func(20))
print(func(15))
print(func(247))