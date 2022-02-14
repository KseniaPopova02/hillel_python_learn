# добавляет элемент в множество
a = set()
a.add(7)
print(a)

# добавляет несколько элементов или все уникальные значения
b = set()
b.update([(1, 2, 3), "hello"])
print(b)

# удаляет объект из множества, при этом не возвращает ошибку, если ввести не существующий объект
b.discard('hello')
print(b)

# удаляет объект, но если написать несуществующий объект, вернет ошибку
g = set("hello")
b.update([(1, 2, 3), "hi"])
print(g)
g.remove("h")
print(g)

# удаляет произвоьный элемент из множества + возвращает удаленный элемент
g.pop()
print(g)

# очищает множество
b.clear()
print(b)

# копирует множество
x = set('abc')
y = x
z = x.copy()
x.add('d')  # изменения в x
print(x)
print(y)  # повлияет на y
print(z)  # не повлияет на z

#Возвращает элементы множества которые отсутствуют в указанном множестве x
l = set('abcdef')
k = set('defghi')
print(k.difference(l))

#Удаляет указанный элемент a, если он присутствует в множестве. Если указанного элемента нет в множестве, то это не приводит к ошибке.
X = set('abcd')
X.discard('a')
print(X)

#Возвращает множество с элементам присутствующими в обоих множествах.
Y = set('abcdef')
X = set('defghi')
print(Y.intersection(X))

#Возвращает True если у множества нет общих элементов с указанным множеством x
Y = set('abc')
X = set('def')
print(Y.isdisjoint(X))

#Возвращает True если множество эквивалентно указанному множеству x или является его подмножеством.
Y = set('abc')
X = set('abc')
print(Y.issubset(X))

#Возвращает True если множество эквивалентно указанному множеству x или является его надмножеством.
Y = set('abc')
X = set('abc')
print(Y.issuperset(X))
Y.add('z')
print(Y.issuperset(X))

#Возвращает объединение множеств.
Y = set('abcdef')
X = set('defghi')
print(Y.union(X))


