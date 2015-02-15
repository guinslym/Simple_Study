#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:9000')
print 'public():',proxy.prefix.public()
try:
    print 'private():',proxy.proxy.private()
except Exception, err:
    print '\nERROR:',err
try:
    print 'public() without prefix:',proxy.public()
except Exception, err:
    print '\nERROR:',err