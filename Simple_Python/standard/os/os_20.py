#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
import sys
import time

for i in range(2):
    print 'PARENT %s:Forking %s' %(os.getpid(),i)
    worker_pid = os.fork()
    if not worker_pid:
        print 'WORKER %s: Starting' % i
        time.sleep(2 + i)
        print 'WORKER %s:Finishing' % i
        sys.exit(i)

for i in range(2):
    print 'PARENT:Waiting for %s' % i
    done = os.wait()
    print 'PARENT:Child done:',done