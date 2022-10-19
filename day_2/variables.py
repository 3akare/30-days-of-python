#!/usr/bin/env python3
'''
Day TWO
30-days-of-python
'''

# Level 1
first_name = 'David'
last_name = 'Bakare'
Fullname = first_name + last_name
country = 'Nigeria'
city = 'Abuja'
Age = 19
year = 2022
is_married = False
is_true = True
is_light_on = True
seconds, minutes, hours = 120, 3200, 45


# Level 2
print(type(first_name))
print(type(last_name))
print(type(Fullname))
print(type(country))
print(type(city))
print(type(Age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(seconds))
print(type(minutes))
print(type(hours))


print(len(first_name))
print(len(first_name) > len(last_name))

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two = num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one // num_two

print('''Total: {}\nDiff: {}\nProduct: \
{}\nDivision: {}\nRemainder: {}\nExp: \
{}\nFloor_Division\
)'''.format(total, diff, product, division, remainder, exp, floor_division))

area_of_circle = 22/7 * (30 ** 2)
print(area_of_circle)
circum_of_circle = 2 * 22/7 * 30
print(circum_of_circle)
radius = int(input("Enter Area: "))
print("Area: {}".format(22/7 * (radius ** 2)))

first_name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
print("Name: {}, Age: {}".format(first_name + last_name, age))
