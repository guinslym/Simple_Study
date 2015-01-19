#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import collections

d=collections.deque("abcdefg")
print "Deque:",d
print "Length:",len(d)
print "Left end:",d[0] #a
print "Right end:",d[-1] #g

d.remove('c')
print 'remove(c):',d