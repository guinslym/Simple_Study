#! /usr/bin/env/python
# -*- coding:utf-8 -*-

try:
    print eval('five times three')
except SyntaxError, err:
    print 'Syntax Error %s (%s-%s):%s' % (err.filename,err.lineno,err.offset,err.text)
    print err