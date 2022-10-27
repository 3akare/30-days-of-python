#!/usr/bin/env python3
'''
Day 7
30 days of python
'''
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('twitter')
it_companies.update(['yelp', 'Jumai'])
it_companies.remove('yelp')
it_companies.discard('yelp')
print(it_companies)

C = A.union(B)

print(A.issubset(B))
print(A.isdisjoint(B))
print(C)

n_a = A.union(B)
print(n_a)
n_b = B.union(A)
n_c = n_b.union(n_b)
print(n_c)

n_a.symmetric_difference(n_b)
print(n_a)

del n_a

print(set(age))
li = [0, 'p', 'hello wolt', 0.9]
print(li)

text = 'I am a teacher and I love to inspire and teach people'
text = text.split(' ')
print(set(text))

# remove raises an error if the item is not found in the set while .discard doesn't
