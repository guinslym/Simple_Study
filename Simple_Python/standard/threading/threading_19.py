# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import threading
import logging
import time

logging.basicConfig(
	level=logging.DEBUG,
	format='(%(threadName)-10s) %(message)s',
)

def worker_with(lock):
	with lock:
		logging.debug('Lock acquired via with at {0}'.format(time.ctime()))

def worker_no_with(lock):
	lock.acquire()
	try:
		logging.debug('Lock acquired directly at {0}'.format(time.ctime()))
	finally:
		lock.release()

lock = threading.Lock()
w = threading.Thread(target=worker_with,args=(lock,))
nw = threading.Thread(target=worker_no_with,args=(lock,))

w.start()
nw.start()