# -*- coding: utf8 -*-
__author__ = 'yuan'

from xmlrpc.client import ServerProxy,Fault
import os
import sys
from xmlrpc.server import SimpleXMLRPCServer
from urllib.parse import urlparse

SimpleXMLRPCServer.allow_reuse_address=1
MAX_HISTORY_LENGTH=6
UNHANDLED=100
ACCESS_DENIED=200

class UnhandledQuery(Fault):
    def __init__(self,message="Couldn't handle the query"):
        super(UnhandledQuery, self).__init__(UNHANDLED,message)
class AccessDenied(Fault):
    def __init__(self,message="Access denied"):
        super(AccessDenied, self).__init__(ACCESS_DENIED,message)
def inside(dir, name):
    dir = os.path.abspath(dir)
    name = os.path.abspath(name)
    return name.startswith(os.path.join(dir, ''))
def get_port(url):
    name = urlparse(url)[1]
    parts = name.split(':')
    return int(parts[-1])
class Node:
    def __init__(self,url,dirname,secret):
        self.url=url
        self.dirname=dirname
        self.secret=secret
        self.known=set()
    def query(self,query,history=[]):
        try:
            return self._handle(query)
        except UnhandledQuery:
            history=history+[self.url]
            if len(history)>=MAX_HISTORY_LENGTH:raise
            return self._broadcast(query,history)
    def hello(self, other):
        self.known.add(other)
        return 0
    def fetch(self, query, secret):
        if secret != self.secret: raise AccessDenied
        result = self.query(query)
        f = open(os.path.join(self.dirname, query), 'w')
        f.write(result)
        f.close()
        return 0
    def _start(self):
        s = SimpleXMLRPCServer(('', get_port(self.url)), logRequests=False)
        s.register_instance(self)
        s.serve_forever()
    def _handle(self, query):
        dir=self.dirname
        name=os.path.join(dir,query)
        if not os.path.isfile(name):raise UnhandledQuery
        if not inside(dir,name):raise AccessDenied
        return open(name).read()
    def _broadcast(self, query, history):
        for other in self.known.copy():
            if other in history:continue
            try:
                s=ServerProxy(other)
                return s.query(query,history)
            except Fault as f:
                if f.faultCode==UNHANDLED:pass
                else:self.known.remove(other)
            except:
                self.known.remove(other)
        return UnhandledQuery
def main():
    url,directory,secret=sys.argv[1:]
    n=Node(url,directory,secret)
    n._start()
if __name__ == '__main__':
    main()

