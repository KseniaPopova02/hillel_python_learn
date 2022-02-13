text = input('Введите текст')
text = text.lower()

ch_space_end = 'черт '

if text[0:5] == ch_space_end:
    print(ch_space_end.replace(ch_space_end, '#### ') + text[5:], sep=' ')

ch_space_front = ' черт'

if text[-5:]==ch_space_front:
    print(text[:len(text)-5]+text.replace(ch_space_front, " ####"), sep=' ')

