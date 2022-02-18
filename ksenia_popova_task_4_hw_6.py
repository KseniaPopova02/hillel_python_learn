d = {1: 'one', 2: 'two', 3: 'two', 4: "three"}

values = set()
new_d = {}

for k, v in d.items():
    if v not in values:
        new_d.update({k: v})
        values.add(v)
print(new_d)

d1 = {'id1':
    {
        'name': 'Ruslan',
        'class': 1,
        'subjects': {'Math', 'Algorithms', 'English'}
    },
    'id2':
        {
            'name': 'Mark',
            'class': 2,
            'subjects': {'Geometry', 'Java', 'Cooking'}
        },
    'id3':
        {
            'name': 'Ruslan',
            'class': 1,
            'subjects': {'Math', 'Algorithms', 'English'}
        }
}
d1.pop('id3')
print(d1)
