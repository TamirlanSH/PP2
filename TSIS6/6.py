def test_range(n, a, b):
    if n in range(a,b):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(int(input("Number: ")), int(input("First num of range: ")), int(input("Second num of range: ")))