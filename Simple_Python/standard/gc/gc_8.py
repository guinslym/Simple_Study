#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import gc
import pprint
import sys

try:
    threshold = int(sys.argv[1])
except (IndexError,ValueError,TypeError):
    print 'Missing or invalid threshold,using default'
    threshold = 5

class MyObj(object):
    def __init__(self,name):
        self.name = name
        print 'Created',self.name

gc.set_debug(gc.DEBUG_STATS)

gc.set_threshold(threshold,1,1)
print 'Thresholds:',gc.get_threshold()
print 'Clear the collector by forcing a run'
gc.collect()
print

print 'Creating object'
objs = []
for i in range(10):
    objs.append(MyObj(i))