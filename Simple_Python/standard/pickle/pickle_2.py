#! /usr/bin/env/python
# -*- coding:utf-8 -*-

try:
    import cPickle as pickle
except ImportError,e:
    import pickle
import pprint

data = [{'a':'A','b':2,'c':3.0}]
print 'BEFORE:',
pprint.pprint(data)
data_string = pickle.dumps(data)
data2 = pickle.loads(data_string)
print 'AFTER:'
pprint.pprint(data2)

print 'SAME? :',(data is data2)
print 'EQUAL?:',(data == data2)