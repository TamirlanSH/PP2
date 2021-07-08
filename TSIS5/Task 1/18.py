f = open("d:/Документы Тамирлана/KBTU/Summer semester/PP2/PP2code/PP2/TSIS5/Task 1/1.txt",'r')
data = f.read()
data.replace(",", " ")
print(len(data.split(" ")))