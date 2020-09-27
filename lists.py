
states = ['New York', 'New Jersey', 'Connecticut', 'California']
for state in states:
    print(f'Welcome to {state}') # Loops- within loops creating repetative action

pizzas = ['Peperoni', 'Meats', 'Works']
for pizza in pizzas:
    print(f'I like {pizza} pizza')
print( 'I really love pizza')

# ctrl + / - will put highlited section as a comment and can reverse it back

# Making the numerical range

for num in range (5):
    print(f'My current number from range(5): {num}') # will show the range from 0 to 4

for num in range(3, 6):
    print(f'My current number from range(3, 6): {num}') # will show the range of numbers from 3 to 5

# List (iterable)- Mutable >> [4,6,12]
# tuple-mutable >>(4,6,12)- immutable

numbers = list(range(5))# 1. range()>> 0 1 2 3   2. list() >> [0,1,2,3,4]  3. numbers= [0,1,2,3,4]
print(numbers)
from math import *


for num in range (5, 13):
    print( f'Square of : {num**2}')



squares = []
for num in range (5, 13):
    num_sqr = num**2
    squares.append(num_sqr)
    # print(num_sqr)
    # print(squares)
print(squares)

squares = list()
for num in range(5, 13):
    squares.append(num**2)
print(squares)

name = 'Ada Lovelace'
print(name.upper())
print(name.lower())

first_name = 'Ada'
last_name = 'lovelace'
full_name= first_name + " "+ last_name
print(full_name)

print('Hello, '+ full_name.title()+'!')

print('\tPython')

print('Languages: \nPython\nC\nJavaScript')

print('Languages:\n\tPython\n\tC\n\tJavaScript')

print('Languages:\t\nPython\t\nC\t\nJavaScript')

favorite_language='Python   '
favorite_language

name='Eric'
print('Hello ' + name + ' Would you like to learn some Pyuthon today?')
print(name.title())
print(name.upper())
print(name.lower())

print('\tAlbert Einstein once said,"A person who never made a \n\tmistake never tried anything new."')

author ='\tAlbert Einstein'
quote ='"A person who never made a \n\tmistake never tried anything new."'

print(author + " once said, "+ quote)
age=23
message= 'Happy '+ str(age) + 'rd Birthday'
print(message)

print(5+3)
print(4*2)
print(12-4)
print(24/3)


bicycles = ['trek', 'cannondale', 'redline', 'specilaized']
print(bicycles)
print(bicycles[0])
print(bicycles[2].title())
print(bicycles[-1])

message = 'My first bicycle was a ' + bicycles[0].title()+ '.'
print(message)

names= ['james', 'Alisher', 'azamat']
print(names[0].title())
print(names[-1].title())

message = 'Hello ' + names[-1].title() + ' hope this message will fiend you in good health.'
print(message)


motorcycles=['handa', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0]= 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(3, 'Harley')
print(motorcycles)

del motorcycles[3]
print(motorcycles)

poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle.title())

first_owned = motorcycles.pop(0)
print('The first motorcycle i owned was a '+ first_owned.title())

motorcycles.remove('yamaha')
print(motorcycles)

motorcycles=['honda', 'yamaha', 'suzuki']

too_expensive= 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA '+ too_expensive.title() + ' is too expensive for me.')

guests= ['alisher', 'kristina', 'azamat']

print( 'Hello ' + guests[0].title(), 'we will be expecting you for a dinner party promtly at 21:00 on thursday night.')
print( 'Hello ' + guests[1].title(), 'we will be expecting you for a dinner party promtly at 21:00 on thursday night.')
print( 'Hello ' + guests[2].title(), 'we will be expecting you for a dinner party promtly at 21:00 on thursday night.')

print('\nUnfortunatly ' + guests[2].title() + ' can not make it to the party due family surcumstances')

guests[2]='Rudik'

print( '\nHello ' + guests[0].title(), 'we will be expecting you for a dinner party promtly at 21:00 on thursday night.')
print( 'Hello ' + guests[1].title(), 'we will be expecting you for a dinner party promtly at 21:00 on thursday night.')
print( 'Hello ' + guests[2].title(), 'we will be expecting you for a dinner party promtly at 21:00 on thursday night.')

guests.insert(0, 'olga')

guests.insert(2, 'tracy')

guests.append('rudy')

print(guests)


cars=['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

len(cars)

print(len(cars))


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title()+ ', that was a great trick')
    print("I can't wait to see your next trick," + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")


for value in range (1,6):
    print(value)


numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

digits= [1,2,3,4,5,6,7,8,9,10]
min(digits)
print(min(digits))
max(digits)
sum(digits)


squares = [value**2 for value in range (1,11)]
print(squares)


apples= list(range(1,21))


print(min(apples))
print(max(apples))
print(sum(apples))

apples= list(range(1,21,2))
print(apples)

apples= [value**3 for value in range(1,11)]
print(apples)


players = ('charles', 'martina', 'michael', 'florence', 'eli')
print(players[0:3])
print(players[1:4])
print(players[:4])

print('Here are the first three players on my team:')
for player in players [:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods
my_foods.append('cannoli')
friend_food.append('ice cream')
print('My favorite foods are:')
print(my_foods)
print('\nMy favorite foods are:')
print(friend_food)



players = ('charles', 'martina', 'michael', 'florence', 'eli')

for player in players :
    print(player)

print( ' Top three players on the list:')
print(players[:3])
print('Next three best players:')
print(players[1:4])
print('The worst three p[layers:')
print(players[-3:])

my_pizza=['peperoni', 'mushroom','anchovies',]
friend_pizza=my_pizza [:]
my_pizza.append('works')
friend_pizza.append('strambolli')
for pizza in my_pizza:
    print(my_pizza)


print(my_pizza)
print(friend_pizza)
basic_foods = ('noodles', 'pies', 'bread', 'salads', 'soups')
for food in basic_foods:
    print(food)


print(basic_foods)

is_male = False
is_tall = False

if is_male or is_tall:
    print('You are a male or tall or both')
else:
    print("You are neither male nor tall")


cars=['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


requested_topings = 'mushrooms'
if requested_topings != 'anchivies':
    print('Hold the anchovies!')

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ', you can post your response if you wish ')

car = 'subaru'
print("Is car == 'subaru' ? I predict True ")
print("\nIs car == 'audi' ? I predict False")
print(car == 'audi')

age = 17
if age >= 18 :
    print("You are old enough to vote!")
    print("Have you registered yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon you turn 18")

age = 12
if age < 4:
    print("Your admission cost is 0")
elif age < 18 :
    print("Your admission cost is 5")
else:
    print("Your admission cost is 10")

age = 12
if age < 4:
   price = 0
elif age < 18:
    price = 5
else:
   price = 10

print("Your admission cost is $" + str(price) + '.')


age = 12
if age < 4:
   price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
   price = 10

print("Your admission cost is $" + str(price) + '.')



age = 12
if age < 4:
   price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age > 65 :
    price = 5

print("Your admission cost is $" + str(price) + '.')

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'peperoni' in requested_toppings:
    print('Adding peperoni')
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print('\nFinished making your pizza')


alien_color = 'red'


if alien_color == 'green':
    print("You just earned 5 points")
elif alien_color == "red":
    print("You just earned 15 points")
else:
    print("You are earned 10 points")

age = 29

if age < 2:
    stage = 'baby'
elif age >=2 and age <4:
    stage = 'toddler'
elif age >= 4 and age < 13:
    stage ='kid'
elif age >= 13 and age < 20:
    stage = 'teenager'
elif age >= 20 and age < 65:
    stage= 'adult'
else:
    stage = 'elder'


requested_toppings = ['mushrooms', 'green pepers', 'extra cheese']
for requested_topping in requested_toppings:
    print("\nAdding "+ requested_topping+ '.')
print("\nFinished making pizza")


requested_toppings = ['mushrooms', 'green pepers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green pepers':
        print('Sorry we are out of green papers right now')
    else:
        print("Adding "+ requested_topping+ '.')
print("\nFinished making pizza")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("\nAdding "+ requested_topping+ '.')
    print("\nFinished making pizza")
else:
    print('Are you sure you want a plain pizza?')




available_toppings = ['mushrooms', 'green pepers', 'extra cheese', 'olives', 'pineapple', 'peperoni']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('\nAdding '+ requested_topping + '.')
    else:
        print('\nSorry, we do not have ' + requested_topping + '.')
print( '\nFinished making pizza.')

admin_names= ['eric', 'john', 'sam', 'sarah', 'admin']
for admin_name in admin_names :
    if admin_name == 'admin':
         print('\nHello ' + admin_name.title()+ ', would you like to see a status report?')
    else:
        print('\nHello '+ admin_name.title() + ', thank you for logging back so soon.')

admin_names = []
if admin_names:
    for admin_name in admin_names:
        print("Thank you for logging back so soon" + admin_name)
else:
        print('\nWe need to find some users')



current_users = ['eric', 'john', 'sam', 'sarah', 'admin']
new_users = ['Eric', 'chloe', 'SANDRA', 'admin', 'samuel']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('Please choose different user name '+ new_user)
    else:
        print('user name is available ' + new_user)

age = 25
age = int(input( 'Enter your age:'))
if age >= 17:
    print('You are eligible to apply for a Drivers Licence')
else:
    diff= 17 - age
    print(f'You will be eligible to apply for a Drivers License in {diff} years.')
