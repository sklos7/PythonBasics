print("Hello,World!")
phrase = "Giraffe Academy"
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])

# Index
print(phrase.index("G"))
print(phrase.index("Aca"))

# Replace
print(phrase.replace("Giraffe", "Elephant"))


# Numbers
print(2)
print(3+4)
print(3*4+4)
print(3*(4+4))
print(10%3)
my_num = 5
print(my_num)
print(str(my_num) + " my favorite number")
my_num = -5
print(abs(my_num))
print(pow(4, 6)) # 4 in the  power of 6
print(max(4, 6)) # largest number
print(min(4, 6)) # smallest number
print(round(4.7541)) # rounding numbers

### from math import
from math import *

print(floor(4.7541)) # rounds up to the whole number 4
print(ceil(4.7541)) # does the apposite to the floor
print(sqrt(4)) # square root

# User input
name = input("Enter you name:")
print("Hello " + name + "!")
age = input("Enter you age:")
print("Hello " + name + "! You are " + age)

# Building a basic calculator

num1 = input("Enter a number:")
num2 = input("Enter another number:")
result = int(num1) + int(num2) # int - only allows to input the whole number without decimal points

print(result)

num1 = input("Enter a number:")
num2 = input("Enter another number:")
result = float(num1) + float(num2) # allows user to input number with decimal points
print(result)

num1 = input("Enter a number:")
num2 = input("Enter another number:")
result = float(num1) + float(num2) # allows user to input number with decimal points
print(result)

# interactive game mab lip

print("Roses are red")
print("violets are blue")
print("I love you")

print("Roses are {color}")
print("{plural noun} are blue")
print("I love {celebrity}")

color = input('Enter a color: ')
plural_noun = input('Enter a plural noun: ')
celebrity = input('Enter a celebrity: ')

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

# List

friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby'] # can input numbers and boolean in the same list
print(friends) # prints the whole list
print(friends[0]) # prints the first value on the list
print(friends[-1]) # prints the last value on the list
print(friends[1:]) # prints all values starting with 2 value (Starting with Karen)
print(friends[1:2]) # prints the range of values

friends[1]= 'kristina' # replaces the value

# List functions

lucky_numbers= [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']
print(friends)

friends.extend(lucky_numbers) # combines two lists together

friends.append('Creed') # Adds items to the back of the list

friends.insert(2, 'kelly') # inserts the value to the specific place

friends.remove('jim') # removes specific value

friends.clear() # clears the whole list

friends.pop() # removes the last element on the list

print(friends.index('Kevin')) # going to show the index number (in this case is 0)

print(friends.count('Kevin')) # going to show how many Kevins are on that list

friends.sort() # will rearange the list in ascending order (alphabetical)

friends2 = friends.copy() # copies the list

# Tuples

coordinates = (4,5) # this is tuple/ you can not change or modify (immutable)
print(coordinates[0])

coordinates = [] # this is list

#functions

def say_hi():
    print('Hello User')

say_hi()


def say_hi(name):
    print('Hello ' + name)

say_hi('Mike')
say_hi('Steve')

# return statement

def cube(num):
    return num*num*num
print (cube(4))


def cube(num):
    return num*num*num
print (cube(4))