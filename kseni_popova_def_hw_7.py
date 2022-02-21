# 1
def cube(x):
    return 'Куб числа', x, '=', x ** 3


print(cube(5))


# 2
def multiply(a, b):
    return 'Результат умножения', a, 'и', b, '=', a * b


print(multiply(3, 989))


# 3
def words_len_4(a):
    a = str(a)
    if len(a) == 4:
        return (a)
    else:
        return "В слове:", a, "не 4 буквы :( "


print(words_len_4('fofofofo'))


# 4
def my_favourite_dish(a):
    a = str()
    if a == "Pelmeni":
        return 'Correct'
    else:
        return "You are wrong"


print(my_favourite_dish('Carrot'))

# 5
def how_to_make_a_sandwich(a):
    if a == "Bread":
        return "Put some ham"
    else:
        return "Find some bread"
print(how_to_make_a_sandwich("ham"))
