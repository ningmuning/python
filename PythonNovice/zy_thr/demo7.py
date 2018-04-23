# -*- coding: utf8 -*-
__author__ = 'yuan'

f=open(r'somefile.txt')
# for i in range(3):
#     print(str(i)+':'+f.readline(),end='')
# print(f.read(7))
# print(f.read())

lines=f.readlines()
f.close()
lines[1]='is not a\n'
f=open(r'somefile.txt','w')
f.writelines(lines)
f.close()
