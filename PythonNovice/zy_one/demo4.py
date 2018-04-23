# -*- coding: utf-8 -*-
__author__ = 'yuan'

import math
x=1
y=math.sqrt
callable(x)
callable(y)

fibs=[0,1]
for i in range(8):
    fibs.append(fibs[-2]+fibs[-1])
print(fibs)

names=['Mrs.Enity','Mrs.Thing']
n=names[:]
print n is names
print n==names

def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}

storage={}
init(storage)
print(storage)

def lookup(data,label,name):
    return data[label].get(name)
print lookup(storage,'middle','Lie')

def store(data,full_name):
    names=full_name.split()
    if len(names==2):names.insert(1,'')
    labels='first','middle','last'
    for label,name in zip(labels,names):
        people=lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name]=[full_name]

print(storage)
