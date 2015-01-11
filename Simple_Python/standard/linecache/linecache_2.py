#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import linecache
from linecache_data import make_tempfile,cleanup,lorem

filename = make_tempfile()

#Blank lines include the newline
print 'BLANK :%r' % linecache.getline(filename,8)
cleanup(filename)