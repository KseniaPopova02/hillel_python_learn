#Для себя, что бы запомнить
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
sixth = {}
a = {**first, **second}
b = {**third, **fourth}
c = {**a, **b}
d = {**c, **fifth}
print(d)

dictionary = {}
values = set()
# добавляем в новый словарь, словарь first
for k, v in first.items():
    if v not in values:
        dictionary.update({k: v})
        values.add(v)
# добавляем в dictionary словарь, словарь second
for k, v in second.items():
    if v not in values:
        dictionary.update({k: v})
        values.add(v)
# добавляем в dictionary словарь, словарь third
for k, v in third.items():
    if v not in values:
        dictionary.update({k: v})
        values.add(v)
# добавляем в dictionary словарь, словарь fourth
for k, v in fourth.items():
    if v not in values:
        dictionary.update({k: v})
        values.add(v)
# добавляем в dictionary словарь, словарь fifth
for k, v in fifth.items():
    if v not in values:
        dictionary.update({k: v})
        values.add(v)
print(dictionary)
