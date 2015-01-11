#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import subprocess

print 'read:'
proc = subprocess.Popen(['echo','"to stdout"'],stdout=subprocess.PIPE,)
stdout_value = proc.communicate()[0]
print '\tstdout:',repr(stdout_value)