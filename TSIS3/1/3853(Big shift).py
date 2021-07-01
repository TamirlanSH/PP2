a = input().split()
b = []
for i in range(len(a)):
    b.append(int(a[i]))

k = int(input())
k = k % len(b)
if k > 0:
    k = abs(k)
    print(*b[k-1:], end=" ")
    print(*b[0:k-1])
if k <= 0:
    k = abs(k)
    print(*b[-k:], end=" ")
    print(*b[0:-k])