#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from operator import *

class MyObj(object):
    """example class for attrgetter"""
    def __init__(self,arg):
    	super(MyObj,self).__init__()
    	self.arg = arg

    def __repr__(self):
    	return 'MyObj (%s)' % self.arg

l = [MyObj(i) for i in xrange(5)]
print 'Objects  :',l

#Extract the 'arg' value from each object
g = attrgetter('arg')
vals = [g(i) for i in l]
print 'args values:',vals

#Sort using arg
l.reverse()
print 'reversed  :',l
print 'sorted     :',sorted(l,key=g)