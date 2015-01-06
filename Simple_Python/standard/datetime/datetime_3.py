#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import datetime

for m in [1,0,0.1,0.6]:
    try:
        print '%02.1f:' % m,datetime.time(0,0,0,microsecond=m)
    except TypeError, err:
        print 'ERROR:',err