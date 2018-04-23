# -*- coding: utf8 -*-
__author__ = 'yuan'

from math import sqrt
scope={}
exec('sqrt=1',scope)
print(sqrt(4))
print(scope['sqrt'])


