# https://stepik.org/lesson/446698/step/9?unit=437004

# Дополните приведенный код, используя генератор, так, чтобы получить словарь result, состоящий из всех элементов словаря months , в которых ключ и значение поменялись местами.

# Примечание. Выводить содержимое словаря result не нужно.

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

result = {months[i]: i for i in months}
