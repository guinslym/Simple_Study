#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import anydbm

db = anydbm.open('/tmp/example.db','r')
try:
    print 'keys():',db.keys()
    for k,v in db.iteritems():
        print 'Iterating:',k,v
        print 'db["author"] =',db['author']
finally:
    db.close()