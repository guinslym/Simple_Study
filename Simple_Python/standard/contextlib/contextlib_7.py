#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import contextlib

class Door(object):
    def __init__(self):
        print ' __init__()'
    def close(self):
        print ' close()'

print 'Normal Example:'
with contextlib.closing(Door()) as door:
    print ' inside with statement'

print '\nError handling example:'
try:
    with contextlib.closing(Door()) as door:
        print ' raising from inside with statement'
        raise RuntimeError('error message')
except Exception, err:
    print ' Had an error:',err