#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from SimpleXMLRPCServer import SimpleXMLRPCServer
import os

server = SimpleXMLRPCServer(('localhost',9000),allow_none=True)

server.register_function(os.listdir,'dir.list')
server.register_function(os.mkdir,'dir.create')
server.register_function(os.rmdir,'dir.remove')

try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'