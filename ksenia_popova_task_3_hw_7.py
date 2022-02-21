lst1 = [1, 2, 3]
lst2 = [11, 12, 13]
lst3=[lst1[0],lst2[0],lst1[1], lst2[1], lst1[2], lst2[2]]
def lst_returning(lst1, lst2):
    return lst3
print(lst_returning([1, 2, 3], [11, 12, 13]))

def two_in_one(list1:list, list2: list):
    return [element for map_typle in zip(list1, list2) for element in map_typle]
print(two_in_one(lst1, lst2))




