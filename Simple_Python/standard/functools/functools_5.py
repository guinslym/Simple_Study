#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import functools
import inspect
from pprint import pprint

@functools.total_ordering
class MyObject(object):
    def __init__(self,val):
        self.val = val
    def __eq__(self,other):
        print ' testing __eq__(%s,%s)' % (self.val,other.val)
        return self.val == other.val
    def __gt__(self,other):
        print ' testing __gt__(%s,%s)' % (self.val,other.val)
        return self.val > other.val
    def __cmp__(self,other):
        print ' testing __cmp__(%s,%s)' % (self.val,other.val)
        return cmp(self.val,other.val)

print 'Methods:\n'
pprint(inspect.getmembers(MyObject,inspect.ismethod))

a = MyObject(1)
b = MyObject(2)

print '\nComparisons:'
for expr in ['a<b','a<=b','a==b','a>=b','a>b','a==b']:
    print '\n%-6s' % expr
    result = eval(expr)
    print ' result of %s: %s'%(expr,result)