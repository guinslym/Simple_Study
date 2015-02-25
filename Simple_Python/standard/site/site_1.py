#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys
import os
import platform
import site

if 'Windows' in platform.platform():
    SUFFIXES = [
         '',
         'lib/site-packages',
    ]
else:
    SUFFIXES = [
        'lib/python%s/site-packages' % sys.version[:3],
        'lib/site-packages',
    ]
print 'Path prefixes:'
for p in site.PREFIXES:
    print '    ',p

for prefix in sorted(set(site.PREFIXES)):
    print
    print prefix
    for suffix in SUFFIXES:
        print
        print '  ',suffix
        path = os.path.join(prefix,suffix).rstrip(os.sep)
        print '  exists :',os.path.exists(path)
        print ' in path:',path in sys.path