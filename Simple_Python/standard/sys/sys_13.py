#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys

class WithoutAttributes(object):
    pass

class WithAttributes(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        return
without_attrs = WithoutAttributes()
print 'WithoutAttributes:',sys.getsizeof(without_attrs)

with_attrs = WithAttributes()
print 'WithAttributes:',sys.getsizeof(with_attrs)