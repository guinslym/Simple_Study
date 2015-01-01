#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import urllib2

response = urllib2.urlopen('http://localhost:8000')
print 'RESPONSE:',response
print 'URL          :',response.geturl()

headers = response.info()
print 'DATA   :',headers['date']
print '-'*30
print headers

data = response.read()
print 'LENGTH  :',len(data)
print 'DATA      :'
print '-'*30
print data