# -*- coding:utf-8 -*-
# /usr/bin/env/python

import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:9000')
multicall = xmlrpclib.MultiCall(server)
multicall.ping()
multicall.show_type(1)
multicall.show_type('string')

for i,r in enumerate(multicall()):
	print i,r