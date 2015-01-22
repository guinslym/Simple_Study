#! /us/bin/env/python
# -*- coding:utf-8 -*-

import math

print math.sqrt(9.0)
print math.sqrt(3)

try:
    print math.sqrt(-1)
except ValueError, e:
    print 'Cannot compute sqrt (-1):',e