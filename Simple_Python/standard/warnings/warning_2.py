#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import warnings
warnings.simplefilter('error',UserWarning)

print 'Before the warning'
warnings.warn('This is a warning message')
print 'After the warning'