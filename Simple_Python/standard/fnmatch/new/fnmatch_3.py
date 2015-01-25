#! /us/bin/env/python
# -*- coding:utf-8 -*-

import fnmatch
import os
import pprint

pattern = 'fnmatch_*.py'
print 'Pattern :',pattern

files = os.listdir('./fnmatch')

print
print 'Files :'
pprint.pprint(files)

print
print 'Matches :'
pprint.pprint(fnmatch.filter(files,pattern))