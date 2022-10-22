#!/usr/bin/env python3
'''
Day 6
30 days of python
'''

empty_tuple = ()
b_siblings = ('David', 'Olawale')
s_siblings = 'fola'

siblings = list(b_siblings)
siblings.append(s_siblings)
print(siblings)
siblings = tuple(siblings)
print(siblings)
siblings = list(siblings)
siblings.append('Daddy')
siblings.append('Mummy')
siblings = tuple(siblings)
print(siblings)

for i in siblings:
    print(i)

food = ('rice', 'bean')
veg = ('apple', 'orange')
smth = ('table', 'chair')

allk = food + veg + smth
print(allk)
allk = list(allk)
del allk[:-3]
del allk[:-3]
del allk
# print(allk)
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

