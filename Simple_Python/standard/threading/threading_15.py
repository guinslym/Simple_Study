# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import threading
import logging
import time
import random

logging.basicConfig(
	level=logging.DEBUG,
	format='(%(threadName)-10s) %(message)s',
)

class Counter(object):
	"""docstring for Counter"""
	def __init__(self, start=0):
		self.lock = threading.Lock()
		self.value = start

	def increment(self):
		logging.debug('Waiting for lock at {0}'.format(time.ctime()))
		self.lock.acquire()
		try:
			logging.debug('Acquired Lock at {0}'.format(time.ctime()))
			self.value = self.value + 1
		finally:
			self.lock.release()

def worker(c):
	for x in range(2):
		pause = random.random()
		logging.debug('Sleeping %0.02f',pause)
		time.sleep(pause)
		c.increment()
	logging.debug('Done at {0}'.format(time.ctime()))

Counter = Counter()
for i in range(2):
	t = threading.Thread(target=worker,args=(Counter,))
	t.start()

logging.debug('Waiting for worker threads at {0}'.format(time.ctime()))
main_thread = threading.currentThread()
for t in threading.enumerate():
	if t is not main_thread:
		t.join()
logging.debug('Counter:%d',Counter.value)