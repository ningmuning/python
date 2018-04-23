# -*- coding: utf-8 -*-
__author__ = 'yuan'

def confict(state,nextX):
    nextY=len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return False
def queens(num,state):
    if len(state)==num-1:
        for pos in range(num):
            if not confict(state,pos):
                yield pos
print(list(queens(4,[1,3,0])))

import sys
args=sys.argv[1:]
args.reverse()
print(''.join(args))

import webbrowser
webbrowser.open('http://www.python.org')
