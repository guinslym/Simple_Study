#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import time

def worker():
    """worker function"""
    print 'Worker at %s' % time.ctime()
    return