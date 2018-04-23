import pymysql.cursors

# 获取链接
connection=pymysql.connect(host='localhost',
                                   user='root',
                                   password='root',
                                   db='wikiurl',
                                   charset='utf8mb4')

try:
    # 获取会话指针
    with connection.cursor() as cursor:
        # 创建sql语句
        sql = "select `urlname`,`urlhref` from `urls`  where `id` is not null"
        # 执行语句

        # limit用法,一会百度
        # sql = "select `urlname`,`urlhref` from `urls`  limit(0,15) "

        num=cursor.execute(sql)
        # 输出
        print(num)

        # 查询3条数据
        # result=cursor.fetchmany(size=3)
        # print(result)

        # 查询所有数据
        # result=cursor.fetchall()
        # print(result)

        # 读取下一行
        # re=cursor.fetchone()
        # print(re)
finally:
    connection.close()
