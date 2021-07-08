def reverse(a):
    b = ""
    i = len(a)
    while i > 0:
        b += a[i-1]
        i -= 1
    return b
print(reverse("sadiufyh"))
