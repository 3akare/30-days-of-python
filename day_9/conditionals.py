#!/usr/bin/env python3

'''
    Day 9
    30 days of python
'''

age = int(input('Enter you age: '))
if age < 18:
    print(f'you need {18 - age} more years to learn to drive')
else:
     print('You are old enough to learn to drive')

your_age = int(input('Enter your age: '))

(print(f'Your are {your_age - 18} years older') if your_age > 18 else print(f'Im {18 - your_age} years older')) if your_age != 18 else print('We are the same age')

get_b = int(input('Enter a number a: '))
get_a = int(input('Enter a number b: '))

print(f'{get_b} is gt than {get_a}') if get_b > get_a else print(f'{get_a} is gt than {get_b}')



score = int(input('Enter a score: '))
if (score <= 100  and score >= 90):
    print('A')
elif (score <= 89 and score >= 70):
    print('B')
elif (score <= 79 and score >= 60):
    print('C')
elif (score <= 69 and score >= 50):
    print('D')
else:
    print('F')

day = input('Enter month: ')
day = day.lower()
day = day.capitalize()

seasons = {'Autumn':['September', 'October', 'November'],
            'Winter':['December', 'January', 'February'],
            'Spring':['March', 'April', 'May'], 
            'Summer':['June', 'July', 'August']
}

for k in seasons.keys():
    if (day in seasons[k]):
        print(k)
        break

fut = input('Enter an item: ')
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.append(fut) if (fut not in fruits) else print(f'{fut} already exist in ths list')

print(fruits)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(person.get('skills')[2:-2]) if 'skills' in person else print('Not a memeber')

if 'skills' in person:
    if 'Python' in person['skills']:
        print('python')

if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('Frontend developer')
elif 'Node' in person['skills'] and 'Python' in person['skills']:
    print('Backend developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('Fullstack Engineer')
else:
    print('unknown title')

if person['is_marred'] is True:
    print('{} {} lives in {}. He is married'.format(person['first_name'], person['last_name'], person['country']))
