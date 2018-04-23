# -*- coding: utf-8 -*-
__author__ = 'yuan'

class Rectangle(object):
    def __init__(self):
        self.width=0
        self.height=0
    def set_size(self,size):
        self.width,self.height=size
    def get_size(self):
        return self.width,self.height
    size=property(get_size,set_size)
r=Rectangle()
r.width=10
r.height=5
print(r.size)
r.size=150,100
print(r.width)

class MyClass(object):
    @staticmethod
    def smeth():
        print('sss')
    @classmethod
    def cmeth(cls):
        print('fff')
m=MyClass()
m.smeth()
m.cmeth()
