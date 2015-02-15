#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:9000')
print proxy.dir.list('/tmp')