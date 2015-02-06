#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import multiprocessing
import time

def worker():
    """worker function"""
    print 'Worker at %s' % time.ctime()
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()