# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import threading
import logging
import time

logging.basicConfig(
	level=logging.DEBUG,
	format='(%(threadName)-10s) %(message)s',
)

def consumer(cond):
	"""Wait for the condition and use the resource"""
	logging.debug('Starting consumer thread at {0}'.format(time.ctime()))
	t = threading.currentThread()
	with cond:
		cond.wait()
		logging.debug('Resource is available to consumer at {0}'.format(time.ctime()))

def producer(cond):
	"""set up the resource to be used by the consumer"""
	logging.debug('Starting producer thread at {0}'.format(time.ctime()))
	with cond:
		logging.debug('Making resource available at {0}'.format(time.ctime()))
		cond.notifyAll()

condition = threading.Condition()
c1 = threading.Thread(name="Thread C1",target=consumer,args=(condition,))
c2 = threading.Thread(name="Thread C2",target=consumer,args=(condition,))
p = threading.Thread(name="Thread P",target=producer,args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()