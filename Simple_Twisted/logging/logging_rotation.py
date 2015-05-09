# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 07:43:02 2015

@author: tim
"""

from twisted.python import log
from twisted.python import logfile

# Log to /tmp/test.log,rotating every 100 bytes
f = logfile.LogFile('test.log','/tmp',rotateLength=100)
log.startLogging(f)
log.msg('First message')

# Rotate manually
f.rotate()

for i in range(10):
    log.msg('Test message',i)

log.msg('Last message')