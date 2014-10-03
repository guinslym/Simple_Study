# coding:utf-8

import httplib
conn=httplib.HTTPConnection('localhost:80')
conn.request('GET','/music.sql')
'''获取状态码'''
r1=conn.getresponse()
print r1.status,r1.reason
'''获取静态文件的内容'''
data=r1.read()
print data
# 关闭连接资源
conn.close()