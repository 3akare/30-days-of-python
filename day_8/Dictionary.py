#!/usr/bin/env python3
'''
Day 8
30 days of python
'''

dog = dict({})
print(type(dog))

dog = {'name': 'karen', 'color': 'red', 'breed': 'german shepherd', 'legs': 2, 'age':20}

student = {
    'firstname': 'David', 
    'secondname': 'Bakare',
    'Gender': 'M', 
    'Age': 19,
    'Martial Status': False,
    'Skills': ['C', 'Python', 'Javascript', 'many many more'],
    'country': 'NIgeria',
    'city': 'Abuja', 
    'Address': 'Im not putting my address here'
}
print(len(student))

print(type(student.get('Skills')))

print(student['Skills'])
student['Skills'].append('shell scripting')

print(student['Skills'])

print(student.keys())
print(student.values())

print(student.items())
print(student.popitem())

del student

print(dog)
