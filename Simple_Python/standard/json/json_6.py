#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import json

data = [{'a':'张三','b':(2,4),'c':3.0,('d',):'D tuple'}]
print 'First attempt'
try:
    print json.dumps(data)
except (TypeError,ValueError), err:
    print 'ERROR:',err
print
print 'Second attempt'
print json.dumps(data,skipkeys=True)