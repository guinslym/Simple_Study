#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import bz2

original_data = 'This is the original text.'

fmt = '%15s %15s'
print fmt % ('len(data)','len(compressed)')
print fmt % ('-'*15,'-'*15)
for i in xrange(5):
    data = original_data*i
    compressed = bz2.compress(data)
    print fmt % (len(data),len(compressed)),
    print '*' if len(data) < len(compressed) else ''