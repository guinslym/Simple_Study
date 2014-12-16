# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import threading
import logging
import time

logging.basicConfig(
	level=logging.DEBUG,
	format='(%(threadName)-10s) %(message)s',
)

class MyThread(threading.Thread):
	def run(self):
		logging.debug('running at {0}'.format(time.ctime()))
		return

for x in range(5):
	t = MyThread()
	t.start()
