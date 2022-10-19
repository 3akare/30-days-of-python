#!/usr/bin/env python3
import math

'''
Day 3
30-days-of-python
'''

age = 0
height = 0.0
complex_var = complex(0)

base = int(input('Enter the Base: '))
height = int(input('Enter tha Height: '))
print('Area: {}'.format(0.5 * base * height))

side_a = int(input('Enter the side of triangle: '))
side_b = int(input('Enter the side of triangle: '))
side_c = int(input('Enter the side of triangle: '))

print('Perimeter: {}'.format(side_a + side_b + side_c))

length = int(input('Enter the Length: '))
width = int(input('Enter the Width: '))
print('Area: {}'.format(length * width))
print('Perimeter: {}'.format(length + width))

radius = int(input('Enter radius: '))
print('Area: {}'.format((22/7) * (radius**2)))
print('Circumference: {}'.format(2 * (22/7) * radius))

y2, y1, x1, x2 = 10, 2, 2, 6
slope = (y2-y1/x2-x1)
distance = math.sqrt((x1 - x2)**2 + (y2 - y2)**2)
print("Distance: {}".format(distance))

print(len('python') > len('dragon'))
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in '''I hope this course is \
not full of jargon. Use in operator to \
check if jargon is in the sentence.''')
print(str(float(len('python'))))


def even(number):
    if (number % 2 == 0):
        print('True')
        return True
    print('False')
    return False


print(7//3 == int(2.7))
print((isinstance(type('10'), type(10))))
# print(int('9.8') == 10)

hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate_per_hour: '))
print('Your Weekly earning is {}'.format(hours * rate_per_hour))

year = int(input("Enter your age: "))
print("You have lived for {}". format(31, 536, 000 * year))

for i in range(1, 6):
    print(i, end=' ')
    print(int(i/i), end=' ')
    print(i, end=' ')
    print(i**2, end=' ')
    print(i**3, end=' ')
    print("")
