#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
import signal
import subprocess
import time

proc = subprocess.Popen('./atexit_4.py')
print 'PARENT: Pausing before sending signal...'
time.sleep(1)
print 'PARENT: Signaling child'
os.kill(proc.pid, signal.SIGTERM)