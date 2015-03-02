#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os

for i in range(10):
    try:
        print i,os.ttyname(i)
    except OSError as err:
        print
        print ' Formatted   :',str(err)
        print 'Errno            :',err.errno
        print ' String error :',err.strerror
        break