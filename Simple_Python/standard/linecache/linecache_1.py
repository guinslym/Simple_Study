#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import linecache
from linecache_data import make_tempfile,cleanup,lorem

filename = make_tempfile()

#Pick out the same line from source and cache.
#(Notice that linecache counts from 1)
print 'SOURCE:'
print '%r' % lorem.split('\n')[4]
print
print 'CACHE:'
print '%r' % linecache.getline(filename,5)

cleanup(filename)