#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import bz2
import os

data = open('copy.txt','r').read()*(2<<9)
print 'Input contains %d bytes' % len(data)

for i in xrange(1,10):
    filename = 'compress-level-%s.bz2' % i
    with bz2.BZ2File(filename,'wb',compresslevel=i) as output:
        output.write(data)
    os.system('cksum %s' % filename)