from urllib.request import urlopen
from urllib.request import Request
from urllib import request
from urllib import parse

# req=Request('')
# postData=parse.urlencode([
#     (key,value),
# ])
# req.add_header()
# resp=urlopen(req,data=postData.encode('utf-8'))
resp=request.urlopen("http://www.baidu.com")
print(resp.read().decode('utf-8'))
