#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import contextlib

@contextlib.contextmanager
def make_context(name):
    print ' entering:',name
    yield name
    print 'exiting :',name

with contextlib.nested(make_context('A'),
                                  make_context('B')) as (A,B):
    print 'inside with statement:',A,B