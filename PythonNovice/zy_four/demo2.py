# -*- coding: utf8 -*-
__author__ = 'yuan'

from tkinter import *
btn=Button()
def clicked():
    print('I was clicked!')
# btn['command']=clicked()
# btn.config(text='click me!',command=clicked())
Button(text='click me too!',command=clicked()).pack()
mainloop()

Label(text="I'm in the first window").pack()
second=Toplevel()
Label(second,text="I'm in the second window!").pack()
for i in range(10):
    Button(text=i).pack()

# mainloop()
help(Pack.config)
help(Grid.configure)
help(Place.config)