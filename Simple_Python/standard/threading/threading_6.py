# -*- coding:utf-8 -*-
#！/usr/bin/env/python

import logging
import threading
import time

logging.basicConfig(
	level=logging.DEBUG,
	format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

def worker():
	logging.debug('Starting the worker threading at {0}'.format(time.ctime()))
	time.sleep(2)
	logging.debug('Exiting the worker threading at {0}'.format(time.ctime()))

def The_service():
	logging.debug('Starting the worker threading at {0}'.format(time.ctime()))
	time.sleep(3)
	logging.debug('Exiting the worker threading at {0}'.format(time.ctime()))

w = threading.Thread(name='the worker',target=worker)
w2 = threading.Thread(target=worker)
t = threading.Thread(name='the_service',target=The_service)

w.start()
w2.start()
t.start()