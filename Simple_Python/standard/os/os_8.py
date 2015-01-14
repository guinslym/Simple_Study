#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
print 'popen2,cmd as sequence:'
stdin,stdout= os.popen2(['cat','-'])

try:
    stdin.write('through stdin to stdout')
finally:
    stdin.close()

try:
    stdout_value = stdout.read()
finally:
    stdout.close()

print '\tpass through:',repr(stdout_value)