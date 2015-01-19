#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import contextlib

@contextlib.contextmanager
def make_context(name):
    print ' entering:',name
    yield name
    print 'exiting :',name

with make_context('A') as A,make_context('B') as B:
    print 'inside with statement:',A,B