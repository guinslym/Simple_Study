#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import multiprocessing
import time
import sys

def daemon():
    p = multiprocessing.current_process().name
    print 'Starting at %s:' % time.ctime(),p
    sys.stdout.flush()
    time.sleep(2)
    print 'Exiting at %s:' % time.ctime(),p

def non_daemon():
    p = multiprocessing.current_process().name
    print 'Starting at %s:' % time.ctime(),p
    print 'Exiting at %s:' % time.ctime(),p

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon',target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon',target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    d.join()
    n.join()