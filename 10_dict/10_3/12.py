# https://stepik.org/lesson/446696/step/12?unit=437002

# Дополните приведенный ниже код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки text будет подсчитано количество его вхождений.

# Примечание. Выводить содержимое словаря result не нужно

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for el in text:
    if el in result:
        result[el] += 1
    else:
        result[el] = 1
