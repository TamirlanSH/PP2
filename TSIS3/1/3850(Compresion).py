a = input().split()
b = []
for i in range(len(a)):
    b.append(int(a[i]))

s = 0
for i in range(len(b)):
    if (b[i] == 0):
        s += 1
        b.pop(i)

for i in range(s):
    b.append(0)
            

print(b)
print(s)