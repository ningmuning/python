from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
import pymysql.cursors

# 简单爬虫
resp=urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')

# 使用BeautifulSoup去解析
soup=bs(resp,'html.parser')

# 获取所有以/wiki/开头的a标签的href属性
listUrls=soup.find_all('a',href=re.compile('^/wiki/'))

# 输出所有的词条对应名称和url
for url in listUrls:
    # 过滤一切jpg或JPG结尾的url
    if not re.search('\.(jpg|JPG)$',url['href']):
        # 输出url的文字和对应的链接
        # string 只能获取一个
        # get_text() 获取标签下所有的文字
        print(url.get_text(),'<------>','https://en.wikipedia.org',url['href'])
        # 获取数据库连接
        connection=pymysql.connect(host='localhost',
                                   user='root',
                                   password='root',
                                   db='wikiurl',
                                   charset='utf8mb4')

        try:
            # 获取会话指针
            with connection.cursor() as cursor:
                # 创建sql语句
                sql="insert into `urls`(`urlname`,`urlhref`)values(%s,%s)"
                # 执行语句
                cursor.execute(sql,(url.get_text(),"https://en.wikipedia.org"+url['href']))
                # 提交
                connection.commit()
        finally:
            connection.close()

