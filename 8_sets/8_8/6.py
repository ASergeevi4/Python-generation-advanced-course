# https://stepik.org/lesson/445793/step/6?unit=436054

# Используя генератор множеств, дополните приведенный ниже код так, чтобы получить множество, содержащее уникальные слова  строки sentence длиною меньше 4 символов. Результат вывести на одной строке (в нижнем регистре) в алфавитном порядке, разделяя элементы одним символом пробела.

# Примечание. Учтите, что знаки пунктуации не относятся к словам.

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

separators = ',.()][:;]'
set_of_words = {word.strip(separators).lower() for word in sentence.split()}
print(*sorted(word for word in set_of_words if len(word) < 4))
