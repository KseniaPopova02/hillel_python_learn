# Первый способ
my_dict = {}
for i in range(1, 21):
    my_dict[i] = i ** 2
print(my_dict)
print(sum(my_dict.values()))
# Второй способ
d = {i: i ** 2 for i in range(1, 21)}
print(d)
print(sum(d.values()))
