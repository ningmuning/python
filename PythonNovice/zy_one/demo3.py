# -*- coding: utf-8 -*-
__author__ = 'yuan'

from math import sqrt
scope={}
exec('sqrt=1',scope)
t=sqrt(4)
f=scope['sqrt']
print(t)
print(f)

sco={}
sco['x']=2
sco['y']=3
e=eval('x*y',sco)
print(e)

sc={}
exec('x=2',sc)
k=eval('x*x',sc)
print(k)

