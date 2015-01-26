#! /usr/bin/env/python
# -*- coding:utf-8 -*-

try:
    import cPickle as pickle
except ImportError,e:
    import pickle
import pprint

data = [{'a':'A','b':2,'c':3.0}]
print 'DATA:',
pprint.pprint(data)
data_string = pickle.dumps(data)
print 'PICKLE:%r' % data_string