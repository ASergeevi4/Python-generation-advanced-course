# https://stepik.org/lesson/519126/step/12?thread=solutions&unit=511575

# Загадка от Жака Фреско 🐐🌶️

# Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только строки из первого списка.

# Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию загадки от Жака Фреско.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна создать файл с именем answer.txt и вывести в него в алфавитном порядке названия цветов козлов, которые удовлетворяют условию загадки Жака Фреско.

# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

with open('goats.txt', 'r', encoding='utf-8') as goats, open('answer.txt', 'w', encoding='utf-8') as answer:
    for line in goats:
        if line.strip() == 'GOATS':
            break
    my_collection = {}
    for goat in goats:
        my_collection[goat.strip()] = my_collection.get(goat.strip(), 0) + 1
    total_goats = sum([v for v in my_collection.values()])
    for k, v in my_collection.items():
        if v / total_goats > 0.07:
            print(k, file=answer)
