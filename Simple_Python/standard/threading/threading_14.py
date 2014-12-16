# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import threading
import logging
import time

logging.basicConfig(
	level=logging.DEBUG,
	format='(%(threadName)-10s) %(message)s',
)

def wait_for_event(e):
	"""Wait for the event to be set before doing anything"""
	logging.debug('wait_for_event start at {0}'.format(time.ctime()))
	event_is_set = e.wait()
	logging.debug('event set:{0} at {1}'.format(event_is_set,time.ctime()))

def wait_for_event_timeout(e,t):
	"""Wait t seconds and then timeout"""
	while not e.isSet():
		logging.debug('wait_for_event_timeout start at {0}'.format(time.ctime()))
		event_is_set = e.wait(t)
		logging.debug('event set:{0} at {1}'.format(event_is_set,time.ctime()))
		if event_is_set:
			logging.debug('Processing event at {0}'.format(time.ctime()))
		else:
			logging.debug('Doing other working at {0}'.format(time.ctime()))

e = threading.Event()
t1=threading.Thread(name='Block',target=wait_for_event,args=(e,))
t1.start()
t2=threading.Thread(name="nonBlock",target=wait_for_event_timeout,args=(e,2))
t2.start()
logging.debug('Waiting before calling Event.set() at {0}'.format(time.ctime()))
time.sleep(3)
e.set()
logging.debug('Event is set at {0}'.format(time.ctime()))