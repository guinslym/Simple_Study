#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from operator import *

class MyObj(object):
    """Example for operator overloading"""
    def __init__(self,val):
    	super(MyObj,self).__init__()
    	self.val = val
    	return
    def __str__(self):
    	return 'MyObj(%s)' % self.val

    def __lt__(self,other):
    	"""compare for less-than"""
    	print 'Testing %s < %s' % (self,other)
    	return self.val < other.val

    def __add__(self,other):
    	"""add values"""
    	print 'Adding %s + %s' % (self,other)
    	return MyObj(self.val+other.val)

a = MyObj(1)
b = MyObj(2)

print 'Comparison'
print lt(a,b)

print '\nArithmetic:'
print add(a,b)