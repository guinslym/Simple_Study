# -*- coding:utf-8 -*-
# /usr/bin/env/python

import xmlrpclib
import datetime

server = xmlrpclib.ServerProxy('http://localhost:9000')
for t,v in [('boolean',True),
	    ('integer',1),
	    ('float',2.5),
	    ('string','some text'),
	    ('datetime',datetime.datetime.now()),
	    ('array',['a','list']),
	    ('array',('a','tuple')),
	    ('structure',{'a':'dictionary'}),
            ]:
    as_string,type_name,value = server.show_type(v)
    print '%-12s:' % t,as_string
    print '%12s' % '',type_name
    print '%12s' % '',value