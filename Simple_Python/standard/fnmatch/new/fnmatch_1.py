#! /us/bin/env/python
# -*- coding:utf-8 -*-

import fnmatch
import os
pattern = 'fnmatch_*.py'
print 'Pattern :',pattern
print

files = os.listdir('.')
for name in files:
    print 'Filename: %-25s %s' %(name,fnmatch.fnmatch(name,pattern))