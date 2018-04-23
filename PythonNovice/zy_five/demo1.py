# -*- coding: utf8 -*-
__author__ = 'yuan'

# 基于socketserver的极简服务器
from socketserver import TCPServer,StreamRequestHandler
class Handler(StreamRequestHandler):
    def handle(self):
        addr=self.request.getpeername()
        print('Got connection from',addr)
        self.wfile.write('Thank you for connecting')
server=TCPServer(('',1234),Handler)
server.serve_forever()

# 分叉服务器
from socketserver import ForkingMixIn
class Server(ForkingMixIn,TCPServer):pass
class Handler2(StreamRequestHandler):
    def handle2(self):
        addr=self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write('Thank you for connecting')
server2=Server(('',1234),Handler2)
server2.serve_forever()

# 线程化服务器
from socketserver import ThreadingMixIn
class Server3(ThreadingMixIn,TCPServer):pass
class Handler3(StreamRequestHandler):
    def handle3(self):
        addr=self.request.getpeername
        print('Got connection from', addr)
        self.wfile.write('Thank you for connecting')
server3=Server3(('',1234),Handler3)
server3.serve_forever()

