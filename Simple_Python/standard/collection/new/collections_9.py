#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import collections

# Add to the right
d=collections.deque()
d.extend("abcdegf")
print "Extend:",d
d.append("h")
print "Append:",d

# Add to the left
f=collections.deque()
f.extendleft(xrange(8))
print "ExtendLeft:",f
f.appendleft(8)
print "Appendleft:",f