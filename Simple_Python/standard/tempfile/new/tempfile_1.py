#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
import tempfile

print 'Building a filename with PID:'
filename = '/tmp/guess_my_name.%s.txt' % os.getgid()
temp = open(filename,'w+b')
try:
    print 'temp'
    print '  ',temp
    print 'temp.name:'
    print '  ',temp.name
finally:
    temp.close()
    #Clean up the temporary file yourself
    os.remove(filename)

print
print 'TemporaryFile:'
temp = tempfile.TemporaryFile()
try:
    print 'temp:'
    print ' ',temp
    print 'temp.name'
    print ' ',temp.name
finally:
    #Automatically cleans up the file
    temp.close()