a = input().split()
b = []
for i in range(len(a)):
    b.append(int(a[i]))
m = 1001

for i in range(0, len(a)):
    if (b[i] > 0 and b[i] < m):
        m = b[i]

print(m)

