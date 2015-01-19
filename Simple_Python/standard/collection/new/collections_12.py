#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import collections

d=collections.deque(xrange(10))
print "Normal         :",d #deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
d=collections.deque(xrange(10))
d.rotate(2)
print "Right rotation :",d #deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
d=collections.deque(xrange(10))
d.rotate(-2)
print 'Left rotate     :',d