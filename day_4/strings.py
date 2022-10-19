#!/usr/bin/env python3
'''
Day 4
30 days of python
'''

strings = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(strings))
strings = ['Coding', 'For', 'All']
print(' '.join(strings))
company = ' '.join(strings)
strings = company
print(company)

print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[7:14])

print(company.index('Coding'))
print(company.rindex('Coding'))
print('Coding' in company)

company = company.replace('Coding', 'Python')
print(company)
company = company.replace('All', 'Everyone')
print(company)

print(strings.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

print('Coding For All'[0])
print('Coding For All'[13])
print('Coding For All'[10])
print('Coding For All'.index('C'))
print('Coding For All'.index('F'))
print('Coding For All'.rfind('l'))

message = '''You cannot end a sentence with \
because because because is a conjunction'''
print(message.rfind('because'))
print(message.rindex('because'))
print(message[message.index('beca\
use'):message.rindex('because') + len('because')])
print("")

radius = 10
area = 3.14 * radius ** 2

print("Coding For All".startswith("Coding"))
print("Coding For All".endswith("coding"))
print('   Coding For All      ' [3:-6], end='')
print('')
print('30'.isidentifier())
print('Thirty'.isidentifier())
print("# ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
print("")
print('I am enjoying this challenge.\nI just wonder what is next.')
print("")
print("Name\tAge\tCountry\tCity\nDavid\t19\tNigeria\tAbuja".expandtabs())
print("")
print(f'''The area of a circle with radius 10 \
is {int(area)} meters square''')
print("")
print('8 + 6 = {}'.format(8 + 6))
print('8 - 6 = {}'.format(8 - 6))
print('8 * 6 = {}'.format(8 * 6))
print('8 / 6 = {0:0.2f}'.format(8 / 6))
print('8 % 6 = {}'.format(8 % 6))
print('8 // 6 = {}'.format(8 // 6))
print('8 ** 6 = {}'.format(8 ** 6))
