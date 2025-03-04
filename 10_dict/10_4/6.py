# https://stepik.org/lesson/488831/step/6?unit=480067

# Телефонная книга 📒
# Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.

# У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу, которая поможет Тимуру находить все номера определённого друга.

# Формат входных данных
# В первой строке задано одно целое число n — количество номеров телефонов, информацию о которых Тимур сохранил в телефонной книге. В следующих n строках заданы телефоны и имена их владельцев через пробел. В следующей строке записано целое число m — количество поисковых запросов от Тимура. В следующих m строках записаны сами запросы, по одному на строке. Каждый запрос — это имя друга, чьи телефоны Тимур хочет найти.

# Формат выходных данных
# Для каждого запроса от Тимура выведите в отдельной строке все телефоны, принадлежащие человеку с этим именем (независимо от регистра имени). Если в телефонной книге нет телефонов человека с таким именем, выведите в соответствующей строке «абонент не найден» (без кавычек).

# Примечание 1. Телефоны одного человека выводите в одну строку через пробел в том порядке, в каком они были заданы во входных данных.

# Примечание 2. Количество строк в ответе должно быть равно числу m.

# Примечание 3. Телефон — это несколько цифр, записанных подряд, а имя может состоять из букв русского или английского алфавита. Записи не повторяются.

list_of_insert = [[i for i in input().lower().split()] for _ in range(int(input()))]
phone_book = {}
for el in list_of_insert:
    name, phone = el[1], el[0]
    if name in phone_book:
        phone_book[name].append(phone)
    else:
        phone_book[name] = [phone]

for _ in range(int(input())):
    print(*phone_book.get(input().lower(), ['абонент не найден']))


# Another option of solving:

# dct = {}
# for _ in range(int(input())):
#     phone, name = input().lower().split()
#     dct.setdefault(name, []).append(phone)
# for _ in range(int(input())):
#     print(*dct.get(input().lower(), ['абонент не найден']))
        
