#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from SimpleXMLRPCServer import SimpleXMLRPCServer
import os
import inspect

server = SimpleXMLRPCServer(('localhost',9000),logRequests=True)

class DirectoryService:
    def list(self,dir_name):
        return os.listdir(dir_name)
server.register_instance(DirectoryService())

try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'