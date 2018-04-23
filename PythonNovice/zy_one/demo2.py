# -*- coding: utf-8 -*-
import string

__author__ = 'yuan'

# table=str.maketrans('cs','kz')
# 'this is an increable test'.translate(table)

items=[('name','Bob'),('age',18)]
d=dict(items)
s=dict(name='Alice',age=20)
print(s)
print(d)
print(d['name'])

from copy import deepcopy
# deepcopy copy
d={}
d['names']=['Alfred','Bertrand']
c=d.copy()
dc=deepcopy(d)
d['names'].append('Clive')
print(c)
print(dc)

# {}.fromkeys(['name','age'])
# dict.fromkeys(['name','age'],'(unknown)')

dic={
    'title':'Python',
    'author':'Vivi',
}
x={'title':'Java'}
print(dic)
dic.update(x)
print(dic)


