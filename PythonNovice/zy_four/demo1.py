# -*- coding: utf8 -*-
__author__ = 'yuan'

# 两种代码，避免重复代码
# with open(r'somefile.txt') as f:
#     char=f.read(1)
#     while char:
#         process(char)
#         char=f.read(1)
#
# with open(r'somefile.txt') as fp:
#     while True:
#         char=fp.read(1)
#         if not char:break
#         process(char)

f=open('somefile.txt','w')
print('First','line',file=f)
print('Second','line',file=f)
print('Third','and final','line',file=f)
f.close()
lines=list(open('somefile.txt'))
print(lines)
first,second,third=open('somefile.txt')
print(first,second,third)
