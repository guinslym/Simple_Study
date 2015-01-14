#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os

print 'popen,read:'
stdout = os.popen('echo "to stdout"','r')
try:
    stdout_value = stdout.read()
finally:
    stdout.close()
print '\tstdout:',repr(stdout_value)

print '\npopen,write:'
stdin = os.popen('cat -','w')
try:
    stdin.write('\tstdin:to stdin\n')
finally:
    stdin.close()