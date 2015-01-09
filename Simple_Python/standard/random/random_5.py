#! /us/bin/env/python
# -*- coding:utf-8 -*-

import random

print '[1,100]:',
for i in xrange(3):
    print random.randint(1,100)

print '\n[-5,5]:',
for i in xrange(3):
    print random.randint(-5,5),
print