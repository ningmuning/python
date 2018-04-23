# -*- coding: utf-8 -*-
__author__ = 'yuan'

import fileinput,re
scope={}
field_pat=re.compile(r'\[(.+?)\]')
def replacement(match):
    code=match.group(1)
    try:
        return str(eval(code,scope))
    except SyntaxError:
        return ''
lines=[]
for line in fileinput.input():
    lines.append(line)
text=''.join(lines)
print(field_pat.sub(replacement,text))

