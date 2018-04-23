# -*- coding: utf-8 -*-
__author__ = 'yuan'

# import fileinput
# for line in fileinput.input(inplace=True):
#     line=line.rstrip()
#     num=fileinput.lineno()
#     print('{:<50}#{:2d}'.format(line,num))

a={1,2,3}
b={2,3,4}
print a.union(b)
print(a|b)

c=a&b
print(c.issubset(a))
print c<=a

print(c.issuperset(a))
print c>=a

print(a.intersection(b))
print(a&b)

print(a.difference(b))
print(a-b)

print(a.symmetric_difference(b))
print(a^b)

print(a.copy())
print(a.copy() is a)

my_sets=[]
for i in range(10):
    my_sets.append(set(range(i,i+5)))
print reduce(set.union,my_sets)

a=set()
b=set()
# a.add(b) error
a.add(frozenset(b))  # right
