#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import json

data = [{'a':'张三','b':(2,4),'c':3.0}]
print 'DATA  :',data

unsorted = json.dumps(data)
print 'JSON:',json.dumps(data)
print 'SORT:',json.dumps(data,sort_keys=True)

first = json.dumps(data,sort_keys=True)
second = json.dumps(data,sort_keys=True)
print 'UNSORTED MATCH:',unsorted ==first
print 'SORTED MATCH    :',first == second