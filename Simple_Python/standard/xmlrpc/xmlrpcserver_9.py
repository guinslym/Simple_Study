# -*- coding:utf-8 -*-
# /usr/bin/env/python

import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:9000')
try:
	server.raises_exception('A message')
except Exception, err:
	print 'Fault code:',err.faultCode
	print 'Message  :',err.faultString