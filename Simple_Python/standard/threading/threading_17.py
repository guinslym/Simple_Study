# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import threading
import time

lock = threading.Lock()
print 'First try {0} at {1}'.format(lock.acquire(),time.ctime())
print 'Second try {0} at {1}'.format(lock.acquire(0),time.ctime())