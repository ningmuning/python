# -*- coding: utf8 -*-
__author__ = 'yuan'

x=['aardvark','abalone','acme','add','aerate']
x.sort(key=len)# 按key值长度排序
print(x)

y=[9,5,3,6,7]
# y.sort(reverse=1)
# y.sort(reverse=True)
y.sort(reverse=0)
# reverse的值可以换数字1，0，-1试试
# 只有0是从小到大，其他都是倒序
print(y)
