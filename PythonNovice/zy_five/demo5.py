# -*- coding: utf8 -*-
__author__ = 'yuan'

import urllib
response=urllib.request.urlopen('http://www.baidu.com')
print(response.getcode())
cont=response.read()
