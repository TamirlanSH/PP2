import re

data = re.compile(r"\w*\s*?\w*\s*\№?\w*\s*\-?\№?\.?\w*\,?\w*\%?\,?\(?\)?\[?\]?\:?\"?")


f = open("dataPP2.txt", 'r')

text = f.read()


res = re.findall(data, text)

print(res)


f.close()