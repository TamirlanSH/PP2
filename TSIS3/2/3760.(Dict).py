n = int(input())

dict_1 = {}

for i in range(n):
    k, v = input().split()
    dict_1[k] = v
    dict_1[v] = k
print(dict_1[input()])





