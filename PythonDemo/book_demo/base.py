# -*- coding: utf8 -*-
__author__ = 'yuan'

print(repr('hello'))
print(str('world'))
# fourth=input('Year: ')[3]
# 获得参数第四位
# print(fourth)
lst=[]
for i in range(1,11):
    lst.append(i)
print(lst[0:11:2])
# 切片去掉最后的一个索引
print(list('hello'))

a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)
# 能够同时将多个值加在列表末尾

x=[3,1,5,9,4]
y=x.copy()
y.sort()
print(x)
print(y)

p=sorted(x)
print(x)
print(p)

