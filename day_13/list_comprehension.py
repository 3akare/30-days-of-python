#!/usr/bin/env python3

'''
    day 13
    30 day of python
'''
number = [-4, -3, -2, -1, 0, 2, 4, 6]
lint = [i for i in number if i < 0]

list_of_list = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lint = [j for row in list_of_list for i in row for j in i]

lint = [(i, i**0, i, i**2, i**3, i**4, i**5) for i in range(11)]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

tuple_to_str = lambda i: str(i)
sth = lambda j: j[0] + ' ' + j[1]
lint = [ tuple_to_str(sth(i)) for row in names for i in row]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]


cap = lambda j: [i.upper() for i in j]
lint = [(cap(i)) for row in countries for i in row]
for i in lint:
    i.insert(1, i[0][:3])
print(lint)

new_lint = [{'country':(cap(i)[0]), 'city':(cap(i)[1])} for row in countries for i in row]
print(new_lint)



slope = lambda y1, y2, x1, x2: (y2 - y1)/(x2 - x1)
