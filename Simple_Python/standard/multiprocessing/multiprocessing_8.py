#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import multiprocessing
import time

def slow_worker():
    print 'Starting worker at %s' % time.ctime()
    time.sleep(0.1)
    print 'Finished worker at %s' % time.ctime()

if __name__ == '__main__':
    p = multiprocessing.Process(target=slow_worker)
    print 'BEFORE:',p,p.is_alive()

    p.start()
    print 'DURING:',p,p.is_alive()

    p.terminate()
    print 'TERMINATE:',p,p.is_alive()

    p.join()
    print 'JOINED:',p,p.is_alive()