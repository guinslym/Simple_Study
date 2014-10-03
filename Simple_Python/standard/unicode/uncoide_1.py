#-*-coding:utf-8-*-
data="中国人"
d=unicode(data,"utf-8")
print d.encode("utf-8")
print data.decode("utf-8").encode("utf-8")