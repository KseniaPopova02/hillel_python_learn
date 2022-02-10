text = input('Введите текст')
text = text.lower()

ch_space_end = 'черт '

if ch_space_end[0:5] in text:
    print(ch_space_end.replace(ch_space_end, '####') + text[5:])

ch_space_front = ' черт'

if ch_space_front[-5:] in text:
    print(text[:len(text)-5]+text.replace(ch_space_front, "####"), sep=' ')
