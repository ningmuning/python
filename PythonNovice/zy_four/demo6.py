# -*- coding: utf8 -*-
__author__ = 'yuan'

# demo5,demo6分别为服务端，客户端
import socket
s=socket.socket()
host=socket.gethostname()
port=1234
s.connect((host,port))
print(s.recv(1024))
