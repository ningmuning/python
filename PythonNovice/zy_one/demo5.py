# -*- coding: utf-8 -*-
__author__ = 'yuan'

def hello(name,greeting='Hello',punction='!'):
    print('{},{}{}'.format(greeting,name,punction))
hello('Mars')

# tuple
def print_params(*params):
    print(params)
print_params('hello,world!')
print_params(1,2,3)

#dict
def print_para(**params):
    print(params)
print_para(x=1,y=2,t=3)

def pr_params(title,*params):
    print_params(title)
    print_params(params)
pr_params('Love',1,2,3)
