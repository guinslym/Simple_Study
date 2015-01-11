#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import signal
import time
import os

def do_exit(sig,stack):
    raise SystemExit('Exiting')

signal.signal(signal.SIGINT,signal.SIG_IGN)
signal.signal(signal.SIGUSR1,do_exit)

print 'My PID:',os.getpid()
signal.pause()