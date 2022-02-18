lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
s = set()
new_lst = []
for d in lst:
    t = tuple(d.values())
    if t not in s:
        s.add(t)
        new_lst.append(d)
print(new_lst)

