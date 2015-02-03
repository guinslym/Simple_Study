#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import gzip
import os
import hashlib

def get_hash(data):
    return hashlib.md5(data).hexdigest()

data = open('untitled','r').read()*1024
cksum = get_hash(data)

print 'Level Size              Checksum'
print '------   ------------------- -----------------------------------'
print 'data  %10d %s' % (len(data),cksum)

for i in xrange(1,10):
    filename = 'compress-level-%s.gz' % i
    with gzip.open(filename,'wb',compresslevel=i) as output:
        output.write(data)
    size = os.stat(filename).st_size
    cksum = get_hash(open(filename,'rb').read())
    print '%5d %10d %s' % (i,size,cksum)