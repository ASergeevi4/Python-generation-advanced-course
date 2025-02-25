# https://stepik.org/lesson/488830/step/13?unit=480066

# Строковое представление 💬
# Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:

# 0 на zero; 1 на one; 2 на two; 3 на three; 4 на four; 5 на five; 6 на six; 7 на seven; 8 на eight; 9 на nine.

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
my_dict = {}
for i in range(len(numbers)):
    my_dict[i] = numbers[i]

my_input = input()
for c in my_input:
    print(my_dict[int(c)], end=' ')
