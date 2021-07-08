f = open("d:/Документы Тамирлана/KBTU/Summer semester/PP2/PP2code/PP2/TSIS5/Task 1/1.txt",'r')
flist = f.readlines()

print([s.rstrip('\n') for s in flist])