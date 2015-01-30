#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import anydbm

db = anydbm.open('/tmp/example.db','w')
try:
    db['one'] = 1
except TypeError, e:
    print '%s: %s' % (e.__class__.__name__,e)
finally:
    db.close()