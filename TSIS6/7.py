def string_test(s):
    d={"Up":0, "Low":0}
    for c in s:
        if c.isupper():
           d["Up"]+=1
        elif c.islower():
           d["Low"]+=1
        else:
           pass
    print ("Upper case characters : ", d["Up"])
    print ("Lower case Characters : ", d["Low"])

string_test('GYFhgyYIFaiKkssss')