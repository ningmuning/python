# -*- coding: utf-8 -*-
__author__ = 'yuan'

import re
some_text='alpha,beta,,,,gamma    delta'
print(re.split('[,]+',some_text))

print(re.split('[,]+',some_text,maxsplit=2))
# maxsplit指定最多分割多少次

pat='{name}'
text='Dear {name}...'
print(re.sub(pat,'Mr. Gumby',text))

print(re.escape('www.python.org'))

m=re.match(r'www\.(.*)\..{3}','www.python.org')
print(m.group(1))
print(m.start(1))
print(m.end(1))
print(m.span(1))

# 如果没有?，匹配贪婪
emphasis_pattern=r'\*\*(.+?)\*\*'
print(re.sub(emphasis_pattern,r'<em>\1</em>','**this** is **it**'))


