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

def show_value(data):
	try:
		val = data.value
	except AttributeError:
		logging.debug('No value yet at {0}'.format(time.ctime()))
	else:
		logging.debug('value=%s',val)

def worker(data):
	show_value(data)
	data.value = random.randint(1,100)
	show_value(data)

class MyLocal(threading.local):
	def __init__(self,value):
		logging.debug('Initializing %r at %s' % (self,time.ctime()))
		self.value = value

local_data = MyLocal(1000)
show_value(local_data)

for i in range(2):
	t = threading.Thread(target=worker,args=(local_data,))
	t.start()