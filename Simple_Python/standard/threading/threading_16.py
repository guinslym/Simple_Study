# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import threading
import logging
import time

logging.basicConfig(
	level=logging.DEBUG,
	format='(%(threadName)-10s) %(message)s',
)

def lock_holder(lock):
	logging.debug('Starting at {0}'.format(time.ctime()))
	while True:
		lock.acquire()
		try:
			logging.debug('Holding at {0}'.format(time.ctime()))
			time.sleep(1)
		finally:
			logging.debug('Not Holding at {0}'.format(time.ctime()))
			lock.release()
		time.sleep(1)
	return

def worker(lock):
	logging.debug('Starting at {0}'.format(time.ctime()))
	num_tries=0
	num_acquires=0
	while num_acquires <3:
		time.sleep(1)
		logging.debug('Trying to acquire at {0}'.format(time.ctime()))
		have_it = lock.acquire(0)
		try:
			num_tries +=1
			if have_it:
				logging.debug('Iteration %d: Acquired at %s' % (num_tries, time.ctime()))
				num_acquires +=1
			else:
				logging.debug('Iteration %d: Not acquired at %s' % (num_tries,time.ctime()))
		finally:
			if have_it:
				lock.release()
		logging.debug('Done after %d Iterations at %s' % (num_tries,time.ctime()))

lock = threading.Lock()
holder = threading.Thread(target=lock_holder,args=(lock,),name='LockHolder')
holder.setDaemon(True)
holder.start()
worker=threading.Thread(target=worker,args=(lock,),name="Worker")
worker.start()