# -*- coding: utf-8 -*-
__author__ = 'yuan'

def flatten(nested):
    # 包含yield语句都被称为生成器
    for sublist in nested:
        for element in sublist:
            yield element
nested=[[1,2],[3,4],[5]]
for num in flatten(nested):
    print(num)
print(list(flatten(nested)))

g=((i+2)**2 for i in range(2,27))
print(next(g))
print(sum(i**2 for i in range(10)))

def flatten2(nested):
    result=[]
    try:
        try:nested+''
        except TypeError:pass
        else:raise TypeError
        for sublist in nested:
            for element in flatten2(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result
k=[1,2,3]
ft=flatten2(k)
print(ft)

def repeater(value):
    while True:
        new=(yield value)
        if new is not None:
            value=new
p=repeater(10)
print(next(p))
print(p.send('Hello'))
