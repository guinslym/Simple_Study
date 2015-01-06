#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import time

for i in range(6,1,-1):
    print '%s %0.2f %0.2f' % (time.ctime(),time.time(),time.clock())
    print 'sleeping',i
    time.sleep(i)
