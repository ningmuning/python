from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from urllib.request import urlopen

# 获取文档对象
fp=open('dmca.pdf','rb')

# 填上PDF的网址即可
# fp=urlopen('')

# 创建一个与文档关联的解释器
parser=PDFParser(fp)

# PDF文档的对象
doc=PDFDocument()

# 链接解释器和文档
parser.set_document(doc)
doc.set_parser(parser)

# 初始化文档
doc.initialize('')
# 没有密码，空字符串

# 创建PDF资源管理器
resource=PDFResourceManager()

# 参数分析器
laparam=LAParams()

# 创建一个聚合器
device=PDFPageAggregator(resource,laparams=laparam)

# 创建页面解释器
interpreter=PDFPageInterpreter(resource,device)

# 使用文档对象读取内容
for page in doc.get_pages():
    # 使用页面解释器读取
    interpreter.process_page(page)

    # 使用聚合器获得内容
    layout=device.get_result()

    # 继续读取下一页内容
    for out in layout:
        if hasattr(out,'get_text'):
            print(out.get_text())

