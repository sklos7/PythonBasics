alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color']= 'yellow'
print(alien_0)


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print('Original x-position:' + str(alien_0['x_position']))
if alien_0 ['speed'] == 'slow':
    x_increment=1
elif alien_0 ['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment


print('New x-position: ' + str(alien_0['x_position']))

alien_0['speed'] = 'fast'

print('New x-position: ' + str(alien_0['x_position']))

print(alien_0)

print('New x-position: ' + str(alien_0['x_position']))


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


favorite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("Sarah's favorite language is " + favorite_languages ['sarah'].title()+'.')

person_1 = {'first_name': 'Kristina', 'last_name': 'Sidorchuk', 'age': 25, 'city': 'brooklyn'}
print(person_1['first_name'])

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print('\nKey:' + key)
    print('Value:' + value)

for name, language in favorite_languages.items():
    print('\n'+ name.title() + "'s favorite language is " + language.title() + '.')

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(' Hi ' + name.title() + ', I see your favorite language is ' + favorite_languages[name].title() + '!' )

















if 'erin' not in favorite_languages:
    print('Erin, please take our poll')

for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking the poll.')

print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())


rivers = {'nile': 'egypt',
          'Mississippi': 'usa',
          'volga': 'russia'
          }
for name, value in rivers.items() :
    print('\nThe river ' + name.title() + ', runs through the whole country of '+ value.title() + '.')

for name in rivers:
    print(name.title())

for value in rivers.values():
    print(value.title())

if 'john' not in favorite_languages:
    print('john please take a poll')


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points' : 15 }

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens [0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['ponts'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens [:5]:
    print(alien)
print('......................................................................')

print('Total number of aliens: ' + str(len(aliens)))

for alien in aliens:
    print(alien)

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
    }
print('You ordered a ' + pizza['crust'] + '- crust pizza' + ' with the following toppings:')
for topping in pizza ['toppings']:
    print('\t' + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite languages are:")
    for language in languages:
       print('\t' + language.title())




users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        }
    }

for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())