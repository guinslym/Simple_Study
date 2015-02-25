#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys

print 'PATH:'
for name in sys.path:
    if name.startswith(sys.prefix):
        name = '...'+name[len(sys.prefix):]
    print ' ',name
print
print 'IMPORTERS:'
for name,cache_value in sys.path_importer_cache.items():
    name = name.replace(sys.prefix,'...')
    print ' %s: %r' % (name,cache_value)