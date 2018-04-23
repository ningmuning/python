# -*- coding: utf8 -*-
__author__ = 'yuan'

# demo5,demo6分别为服务端，客户端
import socket
s=socket.socket()
host=socket.gethostname()
port=1234
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print('Got connection from',addr)
    c.send('Thank you for connecting')
    c.close()
