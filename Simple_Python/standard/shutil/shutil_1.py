#! /us/bin/env/python
# -*- coding:utf-8 -*-

from shutil import *
from glob import glob

print 'BEFORE:',glob('shutil_1.*')
try:
    copyfile('shutil_1.py','shutil_1_.py.copy')
except IOError, e:
    print e
print 'AFTER:',glob('shutil_1.*')