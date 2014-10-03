__author__ = 'Dog'

#coding=utf-8
#XML����
#SAX����XML�ķ�ʽ��Java�е�SAX������һ������ContentHandler�����м̳У�������startDocument��endDocument����Ϣ
from xml.sax import *
#�����xml.sax���е������з����ͱ���
class UserDecodeHandler(ContentHandler):
#��Java��SAXParser����һ�£�������һ��
	users=None
	map=None
	temp=""
	currenttag=None
	user=None
	#ע��Python�������ʽ��������self��Ϊ��һ������
	def startDocument(self):
		print "start xml document"
		
	def endDocument(self):
		print "end xml document"
	#name=��ǰ����ı�ǩ����attrs��dict�ĸ�ʽ��ű�ǩ����������
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
	#content��ʾ���ڴ����е�����	
	def characters(self,content):
		self.temp+=content
		
#����make_parser��������һ��SAX������
# '''
print "===============SAX��ʽ����XML�ĵ�==================="
parser=make_parser()
handler=UserDecodeHandler()
parser.setContentHandler(handler)
data=""
with open("book.xml") as file:
	data=file.read().strip()
import StringIO
#StringIOģ�����ڽ��ַ���ת���������ݣ�������Java��ByteArrayOutputStream��ByteArrayInputStream
parser.parse(StringIO.StringIO(data))

for item in handler.users:
	print "======================="
	for i in item.items():
		key,value=i
		print key,value.encode("gbk")
#'''
