def printValues(x, y):
	l = list()
	for i in range(x,y):
		l.append(i**2)
	print(l)

a = int(input())
b = int(input())

printValues(a,b)