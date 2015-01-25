#! /us/bin/env/python
# -*- coding:utf-8 -*-

from shutil import *
import os
from StringIO import StringIO
import sys

class VerboseString(StringIO):
    def read(self,n=-1):
        next = StringIO.read(self,n)
        print 'read(%d) bytes' %n
        return next

lorem_ipsum = '''Lorem ipsum dolor sit amet,consectetuer adipiscing elit.
 Vestibulum aliquam mollis dolor,Donec vulputate nunc ut diam.
 Ut rutrum mi vel sem,Vestibulum ante ipsum.'''

print 'Default:'
input = VerboseString(lorem_ipsum)
output = StringIO()
copyfileobj(input,output)

print

print 'All at once:'
input = VerboseString(lorem_ipsum)
output = StringIO()
copyfileobj(input,output,-1)

print

print 'Block of 256:'
input = VerboseString(lorem_ipsum)
output = StringIO()
copyfileobj(input,output,256)