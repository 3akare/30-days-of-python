#!/usr/bin/env python3

'''
    day 10
    30 day of python
'''
i = 0
for i in range(1, 11):
    print(i)

while (i != -1):
    print(10 - i)
    i -= 1

for i in range(8):
    print('#' * i)

for i in range(8):
    for j in range(8):
        print('# ', end='')
    print('')

for i in range(0, 11):
    print(f'{i} x {i} = {i * i}')

for i in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(i)

for i in range(0, 101, 2):
    print(i)
for i in range(1, 101, 2):
    print(i)

r_sum = 0
o_sum = 0
e_sum = 0

for i in range(101):
    r_sum += i
print(r_sum)
for i in range(0, 101, 2):
    e_sum += i
for i in range(1, 101, 2):
    o_sum += i
print(f'the sum of all even is {e_sum}. and the sum of all odds is {o_sum}')
