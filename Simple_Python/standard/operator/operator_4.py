#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from operator import *

a = [1,2,3]
b = ['a','b','c']

print 'a=',a
print 'b=',b

print '\nConstructive:'
print 'concat(a,b):',concat(a,b)
print 'repeat(a,3):',repeat(a,3)

print '\nSearching:'
print 'contains(a,1):',contains(a,1)
print 'contains(b,"d"):',contains(b,"d")
print 'countOf(a,1):',countOf(a,1)
print 'countOf(b,"d"):',countOf(b,"d")
print 'indexOf(a,5):',indexOf(a,1)

print '\nAccess Items:'
print 'getitem(b,1):',getitem(b,1)
print 'getslice(a,1,3):',getslice(a,1,3)
print 'setitem(b,1,"d"):',setitem(b,1,"d")
print ',after b=',b
print 'setslice(a,1,3,[4,5]):',setslice(a,1,3,[4,5])
print ',after a=',a

print '\nDestructive:'
print 'delitem(b,1):',delitem(b,1),',after b=',b
print 'delslice(a,1,3):',delslice(a,1,3),',after a=',a
