# -*- coding:utf-8 -*-
# /usr/bin/env/python

import xmlrpclib
import pprint

class MyObj:
	def __init__(self,a,b):
		self.a = a
		self.b =b
	def __repr__(self):
		return 'MyObj (%s,%s)' % (repr(self.a),repr(self.b))

server = xmlrpclib.ServerProxy('http://localhost:9000')
o = MyObj(1,'b goes here')
print 'o  :',o
pprint.pprint(server.show_type(o))
o2 = MyObj(2,o)
print 'o2  :',o2
pprint.pprint(server.show_type(o2))
