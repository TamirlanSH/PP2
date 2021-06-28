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

#Python Lists

#Exercise 1 (print second item)
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#Exercise 2 replace
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#Exercise 3 add
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#Exercise 4 insert (num) after this num insert
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#Exercise 5 remove some ele
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#Exercise 6 last item
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#Exercise 7 third, fourth, fifth
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#Exercise 8 length
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#Python Tuples

#Exercise 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#Exercise 2 numbers
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#Exercise 3 last item
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#Exercise 4 third, fourth, fifth
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#Python Sets

#Exercise 1 check apple in set
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit")
#Exercise 2 add orange in set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#Exercise 3 Unite fruits and more fruits
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#Exercise 4 remove banana if it's exists
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#Exercise 5 remove banana anyway
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#Python Dictionaries

#Exercise 1 value of model
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))
#Exercise 2 change year
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["year"] = 2020
#Exercise 3 add color with value
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"
#Exercise 4 delete model
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")
#Exercise 5 clear dict
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()

#Python If...Else

#Exercise 1
a = 50
b = 10
if a > b:
    print("Hello World")
#Exercise 2
a = 50
b = 10
if a != b:
    print("Hello World")
#Exercise 3
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")
#Exercise 4
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")
#Exercise 5
c = 30
d = 30
if a == b and c == d:
    print("Hello")
#Exercise 6
if a == b or c == d:
    print("Hello")
#Exercise 7 TAB
if 5 > 2:
    print("Five is greater than two!")
#Exercise 8 one line short form
if 5 > 2: print("Five is greater than two!")
#Exercise 9 if else short form
print("Yes") if 5 > 2 else print("No")

#Python While Loops

#Exercise 1
i = 1
while i < 6:
    print(i)
    i += 1
#Exercise 2
i = 1
while i < 6:
    if i == 3:
        break
    i += 1    
#Exercise 3
#Exercise 4