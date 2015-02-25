#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys
import sys_30

def show_module_details(module):
    print '  message    :', module.message
    print '  __name__   :', module.__name__
    print '  __package__:', module.__package__
    print '  __file__   :', module.__file__
    print '  __path__   :', module.__path__
    print '  __loader__ :', module.__loader__

filename = '/tmp/pymotw_import_example.shelve'
sys.path_hooks.append(sys_30.ShelveFinder)
sys.path.insert(0, filename)

print 'Import of "package":'
import package

print
print 'Examine package details:'
show_module_details(package)

print
print 'Global settings:'
print 'sys.modules entry:'
print sys.modules['package']