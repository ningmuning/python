from urllib.request import urlopen

# 读取txt文档
html=urlopen("https://en.wikipedia.org/robots.txt")

print(html.read().decode('utf-8'))