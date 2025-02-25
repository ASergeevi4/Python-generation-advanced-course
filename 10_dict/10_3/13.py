# https://stepik.org/lesson/446696/step/13?unit=437002

# Дополните приведенный ниже код так, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

new_dict = {}
for el in s.split():
    new_dict[el] = new_dict.get(el, 0) + 1
max_count = max(new_dict.values())
candidates = [k for k, v in new_dict.items() if v == max_count]
result = min(candidates)
print(result)
