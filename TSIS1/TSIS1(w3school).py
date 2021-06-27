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

#Exercise 1 length of x
x = "Hello World"
print(len(x))
#Exercise 2 "H"
txt = "Hello World"
x = txt[0]
#Exercise 3 "llo "
txt = "Hello World"
x = txt[2:5]
#Exercise 4 remove all whitespace at begin and at end
txt = " Hello World"
x = txt.strip()
#Exercise 5 to upper
txt = "Hello World"
txt = txt.upper()
#Exercise 6
txt = "Hello World"
txt = txt.lower()
#Exercise 7
txt = "Hello World"
txt = txt.replace("H", "J")
#Exercise 8
age = 36
txt = "My name is Jonh, and I am {}"
print(txt.format(age))

#Python Booleans

#Exercise 1 True
print(10 > 9)
#Exercise 2 False
print(10 == 9)
#Exercise 3 False
print(10 < 9)
#Exercise 4 True
print(bool("abc"))
#Exercise 5 False
print(bool(0))

#Python Operators

#Exercise 1 Multiplication
print(10 * 5)
#Exercise 2 Divide
print(10 / 2)
#Exercise 3
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit")
#Exercise 4
if 5 != 10:
    print("5 and 10 is not equal")
#Exercise 5
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")