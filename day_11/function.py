#!/usr/bin/python3

'''
    day 11
    30 days of python
'''

def add_sum(a=0, b=0):
    return (a + b)
def area_of_circle(r=0):
    return ((22/7) * r * r)
def add_all_nums(*args):
    sum = 0
    for i in args:
        if (isinstance(i, int)):
            sum += i
        else:
            pass
    return (sum)
def temp_convert(temp):
    return ((temp * (9/5) + 32))
def check_season(seasons, day):
    for k in seasons.keys():
        if (day in seasons[k]):
            print(k)
            break
def slope(x1, y1, x2, y2):
    return ((y2 -y1)/(x2-x1))

def quadratic(a, b, c):
    zero = 0
    for x in range(-99999999, 99999999):
        zero = (a*(x**2) + b*(x) + c)
        if zero == 0:
            print(x)

def print_list(lint):
    for i in lint:
        print(i)
def reverse_list(lint):
    new_list = []
    for i in range(len(lint)):
        new_list.append(lint[len(lint) - i - 1])
    return (new_list)

    
def captialize_list(lint):
    new_list = []
    for i in lint:
        new_list.append(i.capitalize())
    return (new_list)
def add_item(lint, item):
    return (lint.append(item))
def remove_item(lint, item):
    lint.remove(item)
    return (lint)

def sum_of_number(n):
    summy = 0
    for i in range(0, n):
        summy += i
    return (summy)
def sum_of_odd_number(n):
    summy = 0
    for i in range(1, n, 2):
        summy += i
    return (summy)
def sum_of_even_number(n):
    summy = 0
    for i in range(0, n + 1, 2):
        summy += i
    return (summy)
def even_and_odd(n):
    odd_summy = 0
    even_summy = 0

    for i in range(0, n + 1, 2):
        even_summy += 1
    for i in range(1, n, 2):
        odd_summy += 1
    return (odd_summy, even_summy)
def factorial(n):
    fact = 1
    for i in range(n):
        fact *= n - i
    return fact
def is_empty(n):
    if (n == None):
        print('Empty')

def unique(lint, item):
    if item in lint:
        return False
    return True
def same_data_type(lint, data):
    for i in lint:
        if not isinstance(i, data):
            return False
    return True

def mean(lint):
    return(sum(lint)/len(lint))

def medain(lint):
    length = len(lint)
    sum = 0
    length = int(length/2)
    if lint[length:(length * -1)] == []:
        for i in lint[length -1:(length - 1 * -1)]:
            sum += i
        return (sum/2)
    for i in lint[length:(length * -1)]:
        return i

def range_int(lint):
    return (max(lint) - min(lint))
