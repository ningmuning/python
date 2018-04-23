# -*- coding: utf-8 -*-
__author__ = 'yuan'

from heapq import *
from random import shuffle
data=list(range(10))
shuffle(data)
heap=[]
for n in data:
    heappush(heap,n)
print(heap)
heappush(heap,0.5)
print(heap)

print(heappop(heap))
hosp=[5,8,0,3,6,7,9,1,4,2]
heapify(hosp)
print(hosp)

heapreplace(hosp,0.5)
print(hosp)

from collections import deque
q=deque(range(5))
q.append(5)
q.appendleft(6)
print(q)
print(q.pop())
print(q.popleft())
q.rotate(3)
print(q)
q.rotate(-1)
print(q)

