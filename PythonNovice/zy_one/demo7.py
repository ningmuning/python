# -*- coding: utf-8 -*-
__author__ = 'yuan'

parameter=10
def combine(parameter):
    print(parameter+globals()['parameter'])
combine(10)

def multiplier(factor):
    def mul(number):
        return number*factor
    return mul
double=multiplier(2)
# mul(2)
print(double(5))

def factorial(n):
    result=n
    for i in range(1,n):
        result*=i
    return result

def factor(n):
    if n==1:
        return 1
    else:
        return factor(n-1)*n
print(factorial(6))
print(factor(6))

def power(x,n):
    result=1
    for i in range(n):
        result*=x
    return result
def power2(x,n):
    if n==0:
        return 1
    else:
        return x*power2(x,n-1)
print(power(3,2))
print(power2(3,2))

def search(sequence,number,lower,upper):
    if lower==upper:
        assert number==sequence[upper]
        return upper
    else:
        middle=(lower+upper)//2
        if number>sequence[middle]:
            return search(sequence,number,middle+1,upper)
        else:
            return search(sequence,number,lower,middle)

seq=['foo','x33','?!','***']
def func(x):
    return x.isalnum()
print(list(filter(func,seq)))
print(filter(lambda x:x.isalnum(),seq))

numbers=[1,2,5,4,8,6]
from functools import reduce
print(reduce(lambda x,y:x+y,numbers))
