#! /us/bin/env/python
# -*- coding:utf-8 -*-

from shutil import *
import os

os.mkdir('example')
print 'BEFORE:',os.listdir('example')
try:
    copy('shutil_1.py','example')
except IOError,e:
    print e
print 'AFTER:',os.listdir('example')