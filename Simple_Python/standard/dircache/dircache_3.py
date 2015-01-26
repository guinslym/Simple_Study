#! /us/bin/env/python
# -*- coding:utf-8 -*-

import dircache

path = '/tmp'
first = dircache.listdir(path)
dircache.reset()
second = dircache.listdir(path)

print 'Identical :',first is second
print 'Equal     :',first == second
print 'Difference:',list(set(second) - set(first))