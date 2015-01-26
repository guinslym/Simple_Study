#! /usr/bin/env/python
# -*- coding:utf-8 -*-

try:
    import cPickle as pickle
except:
    import pickle
import sys

class SimpleObject(object):
    def __init__(self,name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backward = ''.join(l)
        return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

filename = sys.argv[1]
with open(filename,'wb') as out_s:
    # Write to the stream
    for o in data:
        print 'WRITING:%s (%s)' % (o.name,o.name_backward)
        pickle.dump(o,out_s)