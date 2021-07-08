f = open("d:/Документы Тамирлана/KBTU/Summer semester/PP2/PP2code/PP2/TSIS5/Task 1/1.txt", "r")
n = int(input())
for i in range(n-1):
    f.readline()

print(f.readline())