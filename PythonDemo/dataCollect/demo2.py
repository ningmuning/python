from bs4 import BeautifulSoup as bs
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup=bs(html_doc,'html.parser')

# print(soup.prettify())
# 文本全部输出

# print(soup.title.string)
# 输出标题

# print(soup.a)

# print(soup.find(id='link2'))

print(soup.find(id='link2').string)
print(soup.find(id='link2').get_text())

# print(soup.find_all('a'))

for link in soup.find_all('a'):
    print(link.string)
# 获取所有a标签的内容

# print(soup.find('p',{'class':'story'}))
# print(soup.find('p',{'class':'story'}).get_text())

# print(soup.find('p',{'class':'story'}).string)
# 因为p标签里面还有其他标签，需要用get_text()

for tag in soup.find_all(re.compile('^b')):
    print(tag.name)

data=soup.find_all('a',href=re.compile(r'^http://example\.com/'))
# \转译

print(data)

# print(soup.find_all('a').get_txet())
# 错误

# print(soup.find(class='story'))
# 错误，class是关键字
