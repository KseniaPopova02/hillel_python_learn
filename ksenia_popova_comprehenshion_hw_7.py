# list comprehension
# 1
n = 10
a = [x ** 3 for x in range(n)]
print(a)
# 2
a = [100 for x in range(10)]
print(a)
# 3
a = [x % 4 for x in range(50)]
print(a)
# 4
a = [x % 2 == 0 for x in range(5)]
print(a)
# 5
a = [i for i in "Hello"]
print(a)
# DICT comprehension
# 1
a = {i: i ** 2 for i in range(1, 10)}
print(a)
a = {word: len(word) for word in ['Hello', 'I am', 'python', 'dev']}
print(a)
# 2
R = range(0, 11, 2)
D = {t: t + t for t in R}
print(D)
# 3
S = ['dfg', 'gfb', 'argreg', 'ghth', 'jaerga', 'ahre']
S2 = [t for t in S if len(t) > 4]
L = range(1, len(S2) + 1)
D = {k: v for (k, v) in zip(L, S2)}
print(D)
# 4
a = {k: v for k, v in enumerate('hello')}
print(a)
# 5
a = [(k, v) for v, k in enumerate("Hello, World!") if k == 'l']
print(a)
# set comprehensions
# 1
a = {i for i in range(1, 10)}
print(a)
# 2
a = {i for i in "hello"}
print(a)
# 3
a = {i for i in ['hello', 'hello', 'world', 'bye', 'bye']}
print(a)
# 4
a = {i: k for i in [1, 2, 3, 4] for k in [11, 22, 33, 44]}
print(a)
# 5
a = {(i, k) for i in "hello" for k in "world"}
print(a)
