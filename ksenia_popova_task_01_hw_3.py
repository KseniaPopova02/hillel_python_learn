age = input("What's your year of birth?")
if age.isdigit():
    age = int(age)
    if age == 2001:
        print("You should visit Holland.")
    elif age < 2001:
        print("You should visit Vietnam.")
    else:
        print("You can travell everywhere.")
else:
    print('Please write ONLY number')


 
