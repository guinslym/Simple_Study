#! /usr/bin/env/python
# -*- coding:utf-8 -*-

try:
    f = open('/does/not/exist','r')
except IOError as err:
    print 'Formatted  :',str(err)
    print 'Filename    :',err.filename
    print 'Errno          :',err.errno
    print 'String error:',err.strerror