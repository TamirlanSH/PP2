#split()
import re
s = input()
list = re.split("[.,]",s)
for x in list:
    if x:
        print (x)