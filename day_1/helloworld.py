#!/usr/bin/env python3
import math

'''
Day ONE
30-days-of-python
'''


# Level 1 & 2

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)
print('David')
print('Bakare')
print('Nigeria')
print('I am enjoying 30 days of python')

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['David', 'Python', 'Nigeria']))
print(type('David'))
print(type('Bakare'))
print(type('Nigeria'))


# Level 3

print(type(3))  # int
print(type(3j))  # complex
print(type(True))  # boolean
print(type('type'))  # string
print(type([1, 23, 4]))  # list
print(type({'p': 9, 'l': 8}))  # dict
print(type((1, 2, 3, 4)))   # tuple
print(type({2, 3, 4, 5}))   # set

x, y = (2, 3)
x2, y2 = (10, 8)
print(math.sqrt((x - x2)**2 + (y - y2)**2))
