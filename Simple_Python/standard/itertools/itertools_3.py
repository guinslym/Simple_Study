#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from itertools import *

print 'Stop at 5:'
for i in islice(count(),5):
    print i,
print '\n'

print 'Start at 5,Stop at 10:'
for i in islice(count(),5,10):
    print i,
print '\n'

print 'By tens to 100:'
for i in islice(count(),0,100,10):
    print i,
print '\n'