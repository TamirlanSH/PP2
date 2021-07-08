flags = ['flagI', 'flagG', 'flagS', 'flagQ', 'flagP', 'flagO']
with open("d:/Документы Тамирлана/KBTU/Summer semester/PP2/PP2code/PP2/TSIS5/Task 1/1.txt", "w") as myfile:
    for c in flags:
        myfile.write("%s\n" % c)

content = open("d:/Документы Тамирлана/KBTU/Summer semester/PP2/PP2code/PP2/TSIS5/Task 1/1.txt")
print(content.read())