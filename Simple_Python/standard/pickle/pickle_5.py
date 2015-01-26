#! /usr/bin/env/python
# -*- coding:utf-8 -*-

try:
    import cPickle as pickle
except:
    import pickle
import pprint
from cStringIO import StringIO
import sys
from pickle_4 import SimpleObject

filename = sys.argv[1]

with open(filename,'rb') as in_s:
    # Read the data
    while True:
        try:
            o = pickle.load(in_s)
        except EOFError:
            break
        else:
            print 'READ:%s (%s)' % (o.name,o.name_backward)