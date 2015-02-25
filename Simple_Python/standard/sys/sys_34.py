#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys
import sys_30

filename = '/tmp/pymotw_import_example.shelve'
sys.path_hooks.append(sys_30.ShelveFinder)
sys.path.insert(0,filename)

try:
    import package.module3
except ImportError, e:
    print 'Failed to import:',e