# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import threading
import logging
import time

logging.basicConfig(
	level=logging.DEBUG,
	format='(%(threadName)-10s) %(message)s',
)

def delayed():
	logging.debug('Worker running at {0}'.format(time.ctime()))
	return

t1 = threading.Timer(3,delayed)
t1.setName('Threading t1')
t2 = threading.Timer(3,delayed)
t2.setName('Threading t2')

logging.debug('Starting timers at {0}'.format(time.ctime()))
t1.start()
t2.start()

logging.debug('Waiting before canceling {0} at {1}'.format(t2.getName(),time.ctime()))
time.sleep(2)
logging.debug('Canceling {0} at {1}'.format(t2.getName(),time.ctime()))
t2.cancel()
logging.debug('Done at {0}'.format(time.ctime()))