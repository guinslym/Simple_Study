#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import linecache
from linecache_data import make_tempfile,cleanup,lorem

filename = make_tempfile()

#The cache always returns a string,
#and uses an empty string to indicate a line which does not exist

not_there = linecache.getline(filename,500)
print 'NOT THERE:%r includes %d characters' % (not_there,len(not_there))