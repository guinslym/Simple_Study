#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import filecmp
import pprint

dc = filecmp.dircmp('example/dir1','example/dir2')
print 'Common:'
pprint.pprint(dc.common)

print '\nFiles:'
pprint.pprint(dc.common_dirs)

print '\nFiles:'
pprint.pprint(dc.common_files)

print '\nFunny:'
pprint.pprint(dc.common_funny)