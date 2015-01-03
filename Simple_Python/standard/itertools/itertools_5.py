#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from itertools import *

r = islice(count(),5)
i1,i2 = tee(r)
print 'r:',
for i in r:
    print i
    if i>1:
        break
print

print 'i1:',list(i1)
print 'i2:',list(i2)