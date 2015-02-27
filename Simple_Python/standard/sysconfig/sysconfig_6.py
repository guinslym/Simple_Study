#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sysconfig
import pprint
import os

for scheme in ['posix_prefix','posix_user']:
    print scheme
    print '='*len(scheme)
    paths = sysconfig.get_paths(scheme=scheme)
    prefix = os.path.commonprefix(paths.values())
    print 'prefix = %s\n' % prefix
    for name,path in sorted(paths.items()):
        print '%s\n .%s' % (name,path[len(prefix):])
    print