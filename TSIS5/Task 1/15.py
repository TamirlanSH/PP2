import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line("d:/Документы Тамирлана/KBTU/Summer semester/PP2/PP2code/PP2/TSIS5/Task 1/1.txt"))