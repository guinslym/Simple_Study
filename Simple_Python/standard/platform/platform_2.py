#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import platform

print 'Normal  :',platform.platform()
print 'Aliased  :',platform.platform(aliased=True)
print 'Terse    :',platform.platform(terse=True)