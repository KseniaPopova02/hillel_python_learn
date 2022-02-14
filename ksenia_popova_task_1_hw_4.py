line=input('Введите строку:')
print(line[0:2]+line[11:13])
if len(line)<2:
    print("Your line: %s, is too short" % line)
