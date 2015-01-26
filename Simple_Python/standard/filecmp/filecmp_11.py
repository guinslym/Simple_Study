#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import filecmp

dc = filecmp.dircmp('example/dir1','example/dir2')
print 'Subdirectories  :'
print dc.subdirs