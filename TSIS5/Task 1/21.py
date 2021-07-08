import string
def letters_file_line(n):
   with open("d:/Документы Тамирлана/KBTU/Summer semester/PP2/PP2code/PP2/TSIS5/Task 1/1.txt", "w") as f:
       alphabet = string.ascii_uppercase
       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
       f.writelines(letters)
letters_file_line(3)