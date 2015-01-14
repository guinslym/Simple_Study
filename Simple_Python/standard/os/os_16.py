#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
import time

print 'Calling...'
os.system('date;(sleep 3;date) &')

print 'Sleeping...'
time.sleep(5)
