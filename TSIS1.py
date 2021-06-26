#PYTHON SYNTAX

#Exercise 1 (print)
print("Hello, world!")
#Exercise 2 (if)
if 5 > 2:
    print("Five is greater than two")

#PYTHON COMMENTS

#Exercise 1
#This is comments
#Exercise 2
"""
One
Two
Three
"""

#PYTHON VARIABLES

#Exercise 1
carname = "Volvo"
#Exercise 2
x = 50
#Exercise 3
x = 5
y = 10
print(x + y)
#Exercise 4
x = 5
y = 10
z = x + y
print(z)
#Exercise 5
myfirst_name = "John"
#Exercise 6
x = y = z = "Orange"
#Exercise 7 (Global variable)
def myfunc():
    global x
    x = "fantastic"
    print("Variable is " + x) 
myfunc()
print("Python is " + x)

#Python Data Types

#Exercise 1
x = 5
print(type(x))
#Exercise 2
x = "Hello world"
print(type(x))
#Exercise 3
x = 20.5
print(type(x))
#Exercise 4
x = ["apple", "banana", "cherry"]
print(type(x))
#Exercise 5
x = ("apple", "banana", "cherry")
print(type(x))
#Exercise 6
x = {"name" : "Jonh", "age" : 36}
print(type(x))
#Exercise 7
x = True
print(type(x))

#Python numbers

#Exercise 1
x = 5
x = float(x)
#Exercise 2
x = 5.5
x = int(x)
#Exercise 3
x = 5
x = complex(x)

#Python strings

#Exercise 1
x = "Hello World"
print(len(x))
#Exercise 2
#Exercise 3
#Exercise 4
#Exercise 5
#Exercise 6
#Exercise 7
#Exercise 8