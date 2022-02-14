password = input("Введите ваш пароль:")
password1 = input("Повторите пароль")
while password1 == password:
    print("Пароль принят")
    break
else:
    print('Пароль неверен')
