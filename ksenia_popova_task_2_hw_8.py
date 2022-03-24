def max_from_two(a: int, b: int):
    return max(a, b)

def finding_max_from_three(a, b, c: int):
    middle = max_from_two(a, b)
    return max_from_two(middle, c)

print(finding_max_from_three(6, 8, 90))
