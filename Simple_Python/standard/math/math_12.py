#! /us/bin/env/python
# -*- coding:utf-8 -*-

import math

for i in [0,1.0,2.0,3.0,4.0,5.0,6.1]:
    try:
        print '{:2.0f} {:6.0f}'.format(i,math.factorial(i))
    except ValueError, e:
        print 'Error computing factorial (%s):' % i,e