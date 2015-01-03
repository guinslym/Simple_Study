#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import bisect
import random

#Use a constant seed to ensure that the same pseudo-random numbers
#are used each time the loop is run,random.seed(1)

print 'New Pos Contents'
print '---'*3

#Generate random numbers and insert them into a list in sorted order
l = []
for i in range(1,15):
    r = random.randint(1,100)
    position = bisect.bisect(l,r)
    bisect.insort(l,r)
    print '{0} {1}'.format(r,position),l