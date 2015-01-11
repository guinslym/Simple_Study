#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import subprocess

print 'One line at a time:'
proc = subprocess.Popen('python repeater.py',
                                      shell=True,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE
                                      )

for i in range(5):
    proc.stdin.write('%d\n' % i)
    output = proc.stdout.readline()
    print output.rstrip()

remainer = proc.communicate()[0]
print remainer
print
print 'All output at once:'
proc = subprocess.Popen('python repeater.py',
                                       shell=True,
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                      )

for i in range(5):
    proc.stdin.write('%d\n' % i)

output = proc.communicate()[0]
print output