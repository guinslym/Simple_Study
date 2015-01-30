#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import anydbm
import whichdb

db = anydbm.open('/tmp/example.db','n')
db['key']='value'
db.close()

print whichdb.whichdb('/tmp/example.db')