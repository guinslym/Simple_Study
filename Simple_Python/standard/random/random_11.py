#! /us/bin/env/python
# -*- coding:utf-8 -*-

import random
import time

r1 = random.Random()
r2 = random.Random()

#Force r2 to a different part of the random period than r1
r2.setstate(r1.getstate())
r2.jumpahead(1024)

for i in xrange(3):
    print '%04.3f %04.3f' % (r1.random(),r2.random())