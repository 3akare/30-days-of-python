#!/usr/bin/env python3
import string
import random

'''
    day 12
    30 days of python
'''

def random_user_id(y=6):
    sing = string.ascii_letters + string.digits
    for i in range(y):
        print(sing[random.randint(0, len(sing) - 1)], end='')
    print('')

def user_id_gen_by_user():
    length = int(input('Enter length of the password: '))
    num = int(input('Enter the number of password to be generated: '))
    for i in range(num):
        random_user_id(length)
def rgb_color_gen():
    return (f'rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})')

def list_of_hexa_colors():
    sing = string.ascii_letters[:6] + string.digits
    new_string =  ''
    new_list = []
    for i in range(7):
        if (i == 0):
            new_string += '#'
        else:
            new_string += sing[random.randint(0, len(sing) - 1)]
    new_list.append(new_string)
    return new_list

def list_of_rgb_colours():
    new_list = []
    for i in range(4):
        new_list.append(rgb_color_gen())
    print(new_list)

def generate_colors(typ, num):
    new_list = []
    for i in range(num):
        if typ == 'hexa':
            new_list.append(list_of_hexa_colors())
        elif typ == 'rgb':
            new_list.append(rgb_color_gen())
    print(new_list)
def unique_rando():
    my_list = []
    while len(my_list) < 7:
        num = random.randint(0, 9)
        if num in my_list:
            continue
        else:
            my_list.append(num)
    print(my_list)

def shuffled_list(lint):
    pass
