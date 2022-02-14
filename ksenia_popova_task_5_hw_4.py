some_lst = ['red', 'white', 'black', 'red', 'green', 'black']
res_lst = []
for item in some_lst:
    if item  not in res_lst:
        res_lst.append(item)
print(sorted(res_lst))

