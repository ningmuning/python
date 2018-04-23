# -*- coding: utf-8 -*-
__author__ = 'yuan'

class Rectangle(object):
    def __init__(self):
        self.width=0
        self.height=0
    def __setattr__(self, name, value):
        if name=='size':
            self.width,self.height=value
        else:
            self.__dict__[name]=value
    def __getattr__(self, name):
        if name=='size':
            return self.width,self.height
        else:
            raise AttributeError()
r=Rectangle()
print(r.__getattr__)
print(r.__setattr__)
print(r.__dict__)
print(r.__init__)
print(r.__delattr__)

class Fibs(object):
    def __init__(self):
        self.a=0
        self.b=1
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self
f=Fibs()
print(f.next())

class TestIterator(object):
    value=0
    def next(self):
        self.value+=1
        if self.value>10:
            raise StopIteration
        return self.value
    def __iter__(self):
        return self
ti=TestIterator()
print(list(ti))
