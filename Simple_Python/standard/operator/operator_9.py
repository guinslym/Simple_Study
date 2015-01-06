#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from operator import *

class NoType(object):
    """Supports none of the type APIs"""

class MultiType(object):
    """Supports multiple type APIs"""
    def __len__(self):
    	return 0
    def __getitem__(self,name):
    	return 'mapping'
    def __int__(self):
    	return 0

o = NoType()
t = MultiType()

for func in (isMappingType,isNumberType,isSequenceType):
    print '%s(o):' % func.__name__,func(o)
    print '%s(t):' % func.__name__,func(t)