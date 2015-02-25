#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys
import sys_30

filename = '/tmp/pymotw_import_example.shelve'
sys.path_hooks.append(sys_30.ShelveFinder)
sys.path.insert(0,filename)

print 'First import of "package":'
import package

print
print 'Reloading "package":'
reload(package)