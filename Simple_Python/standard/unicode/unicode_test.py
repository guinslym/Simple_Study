#coding:utf-8
import sys
a=u"中"
b=a.encode("utf-8")
print b

u='\xc3\x96\xc3\x90'
s=u.decode("utf-8")
print s

print sys.getdefaultencoding()
