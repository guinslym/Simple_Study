#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import json

data = [{'a':'张三','b':(2,4),'c':3.0}]
print 'DATA:',repr(data)

data_string = json.dumps(data)
print 'JSON:',data_string