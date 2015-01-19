#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import array
import binascii

s = 'This is the array.'
a = array.array('c',s)

print 'As string:',s
print 'As array :',a
print 'As hex   :',binascii.hexlify(a)