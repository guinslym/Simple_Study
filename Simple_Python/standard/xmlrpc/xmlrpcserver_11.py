# -*- coding:utf-8 -*-
# /usr/bin/env/python

import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:9000')
multicall = xmlrpclib.MultiCall(server)
multicall.ping()
multicall.show_type(1)
multicall.raises_exception('Next to last call stops execution')
multicall.show_type('string')

try:
    for i,r in enumerate(multicall()):
        print i,r
except xmlrpclib.Fault as err:
    print 'ERROR:',err