#! /usr/bin/env/python
# -*- coding:utf-8 -*-

try:
    import cPickle as pickle
except:
    import pickle
import pprint
from cStringIO import StringIO

class SimpleObject(object):
    def __init__(self,name):
        self.name = name
        self.name_backward = name[::-1]
        return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

# Simulate a file with StringIO
out_s = StringIO()

# write to the stream
for o in data:
    print 'WRITING : %s (%s)' % (o.name,o.name_backward)
    pickle.dump(o,out_s)
    out_s.flush()

# Set up a read-able stream
in_s = StringIO(out_s.getvalue())

# Read the data
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print 'READ :%s (%s)' % (o.name,o.name_backward)