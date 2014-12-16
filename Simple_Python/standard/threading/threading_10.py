# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import threading
import random
import time
import logging

logging.basicConfig(
	level=logging.DEBUG,
	format='(%(threadName)-10s) %(message)s',
)

def worker():
	"""thread worker function"""
	t = threading.currentThread()
	pause = random.randint(1,5)
	logging.debug('Sleeping in {0} seconds,now is {1}'.format(pause,time.ctime()))
	time.sleep(pause)
	logging.debug('ending the sleep,now is {0}'.format(time.ctime()))
	return

for i in range(3):
	t = threading.Thread(target=worker)
	t.setDaemon(True)
	t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
	if t is main_thread:
		continue
	logging.debug('Joining the threading,{0}'.format(t.getName()))
	t.join()