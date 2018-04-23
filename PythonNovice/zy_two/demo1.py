# -*- coding: utf-8 -*-
__author__ = 'yuan'

import abc

class A(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self):
        return
class B(A):
    def load(self):
        print('Hello')

s=B()
s.load()

while True:
    try:
        x=int(input('Enter the first number:'))
        y=int(input('Enter the second number:'))
        value=x/y
        print('x/y is',value)
    except Exception as e:
        print('Invalid input:',e)
        print('Please try again.')
    else:
        break
