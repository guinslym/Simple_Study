#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import anydbm

db = anydbm.open('/tmp/example.db','n')
db['key'] ='value'
db['today'] = 'Sunday'
db['author'] = 'Jack'
db.close()