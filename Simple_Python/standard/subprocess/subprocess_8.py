#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import subprocess

print 'write:'
proc = subprocess.Popen(['cat','-'],stdin=subprocess.PIPE,)
proc.communicate('\tstdin:to stdin\n')