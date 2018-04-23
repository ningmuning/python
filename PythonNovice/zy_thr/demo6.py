# -*- coding: utf8 -*-
__author__ = 'yuan'

# f=open('somefile.txt','w')
# f.write('hello,')
# f.write('world')
# f.close()
# fp=open('somefile.txt','r')
# fp.read(4)
# fp.read()

import sys
text=sys.stdin.read()
words=text.split()
wordcount=len(words)
print('Wordcount:',wordcount)
