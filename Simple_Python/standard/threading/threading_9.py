# -*- coding:utf-8 -*-
#！/usr/bin/env/python

import threading
import time
import logging

logging.basicConfig(
	level=logging.DEBUG,
	format='(%(threadName)-10s) %(message)s',
)

def daemon():
	logging.debug('Starting the threading at {0}'.format(time.ctime()))
	time.sleep(2)
	logging.debug('Exiting the threading at {0}'.format(time.ctime()))

d=threading.Thread(name='daemon threading',target=daemon)
d.setDaemon(True)

def non_daemon():
	logging.debug('Starting the threading at {0}'.format(time.ctime()))
	logging.debug('Exiting the threading at {0}'.format(time.ctime()))

t = threading.Thread(name='Non Daemon threading',target=non_daemon)

d.start()
t.start()

#等待线程1秒如果还没结束,则结束join等待
d.join(1)
print 'd,isAlive()',d.isAlive()
t.join()