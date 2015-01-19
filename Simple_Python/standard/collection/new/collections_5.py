#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import collections

c = collections.Counter()
with open('/home/tim/untitled','rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print 'Most common:'
for letter,count in c.most_common(3):
    print '%s:%7d' % (letter,count)