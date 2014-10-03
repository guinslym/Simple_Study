__author__ = 'Dog'

#coding=utf-8
#XML处理
#SAX处理XML的方式和Java中的SAX解析器一样，从ContentHandler方法中继承，并处理startDocument、endDocument等信息
from xml.sax import *
#必须从xml.sax包中导入所有方法和变量
class UserDecodeHandler(ContentHandler):
#与Java的SAXParser基本一致，处理方法一样
	users=None
	map=None
	temp=""
	currenttag=None
	user=None
	#注意Python的特殊格式，必须有self作为第一个参数
	def startDocument(self):
		print "start xml document"
		
	def endDocument(self):
		print "end xml document"
	#name=当前处理的标签名，attrs以dict的格式存放标签的所有属性
	def startElement(self,name,attrs):
		if name=="book":
			self.users=[]
		elif name=="book":
			self.user={"name":attrs['name']}
		self.currenttag=name
	
	def endElement(self,name):
		if name=="book":
			self.users.append(self.user)
		elif name=="description":
			self.user.update({"description":self.temp.strip()})
			self.temp=""
		self.currenttag=None
	#content表示正在处理中的数据	
	def characters(self,content):
		self.temp+=content
		
#调用make_parser方法创建一个SAX解析器
# '''
print "===============SAX方式解析XML文档==================="
parser=make_parser()
handler=UserDecodeHandler()
parser.setContentHandler(handler)
data=""
with open("book.xml") as file:
	data=file.read().strip()
import StringIO
#StringIO模块用于将字符串转换成流数据，类似于Java的ByteArrayOutputStream和ByteArrayInputStream
parser.parse(StringIO.StringIO(data))

for item in handler.users:
	print "======================="
	for i in item.items():
		key,value=i
		print key,value.encode("gbk")
#'''
