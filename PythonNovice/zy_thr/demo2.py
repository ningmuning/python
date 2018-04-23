# -*- coding: utf-8 -*-
__author__ = 'yuan'

from random import *
from time import *
date=(2016,1,1,0,0,0,-1,-1,-1)
tim=mktime(date)
date2=(2017,1,1,0,0,0,-1,-1,-1)
tim2=mktime(date2)
random_time=uniform(tim,tim2)
print(asctime(localtime(random_time)))

from random import randrange
num=int(input('How many dice?'))
sides=int(input('How many sides per die?'))
sum=0
for i in range(num):
    sum+=randrange(sides)+1
print('The result is',sum)
