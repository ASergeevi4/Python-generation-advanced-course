# https://stepik.org/lesson/483114/step/13?unit=474427

# Урок биологии 🌱

# Даны по 10-балльной шкале оценки по биологии трех учеников. Напишите программу, которая выводит множество оценок, не встречающихся ни у одного из трех учеников.

# Формат входных данных
# На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).

# Формат выходных данных
# Программа должна вывести множество оценок в порядке возрастания на одной строке, разделенных пробелами, в соответствии с условием задачи.

# Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.

grades_1 = set(int(i) for i in input().split())
grades_2 = set(int(i) for i in input().split())
grades_3 = set(int(i) for i in input().split())
result = [i for i in range(11) if i not in (grades_1 | grades_2 | grades_3)]
print(*sorted(result))
