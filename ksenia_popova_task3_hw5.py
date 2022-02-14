# c пользовательским вводом
entered_list = input('Enter your numbers, separated by commas:\n')
list = list(map(int, (entered_list.split(', '))))
counter = 0
while list[counter] % 2 == 0:
    counter += 1
    if counter == len(list):
        print('all numbers are even')
        break
else:
    print('NO')

# Без пользовательского ввода
input('eneter')
a = [7, 80, 78, 67, 10]
while len(a)>0:
    last=a.pop()
    if last % 2 == 0:
        print('All numbers are even')
        break
else:
    print("No")
