# -*- coding: utf-8 -*-
__author__ = 'yuan'

class Bird(object):
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry=False
        else:
            print('No,thanks!')
class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound='Squawk!'
    def sing(self):
        print(self.sound)

sb=SongBird()
sb.sing()
sb.eat()
sb.eat()

class CounterList(list):
    def __init__(self,*args):
        super(CounterList, self).__init__(*args)
        self.counter=0
    def __getitem__(self, index):
        self.counter+=1
        return super(CounterList, self).__getitem__(index)
sc=CounterList(range(10))
print(sc)
print(sc.reverse())
del sc[3:6]
print(sc)
print(sc.counter)