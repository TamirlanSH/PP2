f = open("d:/Документы Тамирлана/KBTU/Summer semester/PP2/PP2code/PP2/TSIS5/Task 1/1.txt", "r")
words = f.read().split()
max_len = len(max(words, key=len))
print([word for word in words if len(word) == max_len])