#!/usr/bin/env python3

'''
    Higher Functions
    30 days of python
'''

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



lint = [countries, names, numbers]
for i in lint:
    for j in i:
        print(j, end=' ')
    print('')
new_count_list = lint[:]
lint = map(lambda x: x.upper(), countries)
print(list(lint))

lint = map(lambda x: x**2, numbers)
print(list(lint))

def filter_land(x):
    return True if 'land' in x else False
def length_country(x):
    return True if len(x) == 6 else False
def length_6_and_more(x):
    return True if len(x) >= 6 else False
def start_with_e(x):
    return True if x[:1] == 'E' else False

function_list = [filter_land, length_6_and_more, length_country, start_with_e]

for i in function_list:
    lint = filter(i, countries)
    print(list(lint))

def get_string_list(x):
    return True if type(x) == str else False

new_count_list = [i for row in new_count_list for i in row]
lint = filter(get_string_list, new_count_list)
print(list(lint))
