#! /us/bin/env/python
# -*- coding:utf-8 -*-

import fnmatch

pattern = 'fnmatch_*.py'
print 'Pattern :',pattern
print 'Regx    :',fnmatch.translate(pattern)