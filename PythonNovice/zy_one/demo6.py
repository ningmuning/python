# -*- coding: utf-8 -*-
__author__ = 'yuan'

def story(**kwds):
    return 'Once upon a time, there was a' \
           '{job} called {name}.'.format(kwds)
def power(x,y,*others):
    if others:
        print('Received redundant parameters:',others)
    return pow(x,y)
def interval(start,stop=None,step=1):
    'Imitates range() for step>0'
    if stop is None:
        start,stop=0,start
    result=[]
    i=start
    while i<stop:
        result.append(i)
        i+=step
    return result

# error don't know
# print(story(job='king',name='Gumby'))
# params={'job':'language','name':'Python'}
# print(story(**params))
# del params['job']
# print(story(job='stroke of genius',**params))
print(power(2,3))
pa=(5,)*2
print(power(*pa))
power(3,3,'Hello,world')
print(interval(10))
print(power(*interval(3,7)))
