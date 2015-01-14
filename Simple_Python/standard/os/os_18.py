#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
import signal
import time

def signal_usrl(signum,frame):
    "Callback invoked when a signal is received"
    pid = os.getpid()
    print 'Received USR1 in process %s' % pid

print 'Forking...'
child_pid = os.fork()
if child_pid:
    print 'PARENT:Pausing before sending signal...'
    time.sleep(1)
    print 'PARENT:Signling %s' % child_pid
    os.kill(child_pid,signal.SIGUSR1)
else:
    print 'CHILD:Setting up signal handler'
    signal.signal(signal.SIGUSR1,signal_usrl)
    print 'CHILD:Pausing to wait for signal'
    time.sleep(5)