# https://stepik.org/lesson/488830/step/14?unit=480066

# Информация об учебных курсах 🎓
#Напишите программу, которая по номеру курса выводит информацию о данном курсе.

my_dict = {}
my_dict['CS101'] = (3004, 'Хайнс', '8:00')
my_dict['CS102'] = (4501, 'Альварадо', '9:00')
my_dict['CS103'] = (6755, 'Рич', '10:00')
my_dict['NT110'] = (1244, 'Берк', '11:00')
my_dict['CM241'] = (1411, 'Ли', '13:00')
my_input = input()
print(f'{my_input}: {my_dict[my_input][0]}, {my_dict[my_input][1]}, {my_dict[my_input][2]}')

# Another option of solving

# course_number = input()  # We're entering number of course
# audience, teacher, time = my_dict[course_number]  # unpack tuple into 3 variables
# print(f'{course_number}: {audience}, {teacher}, {time}') # printing result with f-strings
