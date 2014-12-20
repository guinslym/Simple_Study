# -*- coding:utf-8 -*-
# /usr/bin/env/python

import xmlrpclib
import datetime
import pprint

server = xmlrpclib.ServerProxy('http://localhost:9000')
data = {'boolean':True,
	'integer':1,
	'float':2.5,
	'string':'some text',
	'datetime':datetime.datetime.now(),
	'array':['a','list'],
	'array':('a','tuple'),
	'structure':{'a':'dictionary'},
            }

arg = []
for i in range(3):
    d = {}
    d.update(data)
    d['integer']=i
    arg.append(d)

print 'Before:'
pprint.pprint(arg)

print
print 'After:'
pprint.pprint(server.show_type(arg)[-1])