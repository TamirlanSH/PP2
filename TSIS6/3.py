def sum(list):
    s = 1
    for i in list:
        s *= i
    return s
print(sum((7, 5, 2, -1, 4, 9)))