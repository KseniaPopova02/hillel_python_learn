def words(a):
    a = a.lower()
    if a == a[::-1]:
        return True
    else:
        return False


print(words("Topot"))
