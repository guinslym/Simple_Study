#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
print 'popen4:'
stdin,stdout_and_stderr= os.popen4('cat -;echo ";to stderr" 1>&2')

try:
    stdin.write('through stdin to stdout')
finally:
    stdin.close()

try:
    stdout_value = stdout_and_stderr.read()
finally:
    stdout_and_stderr.close()

print '\tpass through:',repr(stdout_value)