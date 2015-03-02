#! /usr/bin/env/python
# -*- coding:utf-8 -*-

print 'Division:'
try:
    print 1/0
except ZeroDivisionError as err:
    print err

print 'Modulo  :'
try:
    print 1 % 0
except ZeroDivisionError as err:
    print err