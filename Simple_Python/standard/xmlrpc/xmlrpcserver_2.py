# -*- coding:utf-8 -*-
# /usr/bin/env/python

import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:9000',verbose=True,encoding='ISO-8859-1')
print 'Ping:',server.ping(),