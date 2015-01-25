#! /us/bin/env/python
# -*- coding:utf-8 -*-

import fnmatch
import os
pattern = 'FNMATCH_*.py'
print 'Pattern :',pattern
print

files = os.listdir('.')
for name in files:
    print 'Filename: %-25s %s' %(name,fnmatch.fnmatchcase(name,pattern))