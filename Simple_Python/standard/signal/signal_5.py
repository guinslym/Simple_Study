#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import signal
import time
import os
import threading

def signal_handler(num,stack):
    print 'Received signal %d in %s' % (num,threading.currentThread().name)

signal.signal(signal.SIGUSR1,signal_handler)

def wait_for_signal():
    print 'Waiting for signal in',threading.currentThread().name
    signal.pause()
    print 'Done waiting'

# Start a thread that will not receive the signal
receiver = threading.Thread(target=wait_for_signal,name='receiver')
receiver.start()
time.sleep(0.1)

def send_signall():
    print 'Sending signal in',threading.currentThread().name
    os.kill(os.getpid(),signal.SIGUSR1)

sender = threading.Thread(target=send_signall,name='sender')
sender.start()
sender.join()

# Waiting for the thread to see the signal (not going to happen!)
print 'Waiting for',receiver.name
signal.alarm(2)
receiver.join()