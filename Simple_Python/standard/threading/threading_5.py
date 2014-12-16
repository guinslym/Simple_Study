# -*- coding:utf-8 -*-
#！/usr/bin/env/python

import threading
import time

def worker():
	"""thread worker function"""
	print threading.currentThread().getName(),' Starting at {0}'.format(time.ctime())     #currentThread()返回当前的Thread对象
	time.sleep(2)
	print threading.currentThread().getName(),' Exiting at {0}'.format(time.ctime())

def my_service():
	print threading.currentThread().getName(),' Starting at {0}'.format(time.ctime())
	time.sleep(3)
	print threading.currentThread().getName(),' Exiting at {0}'.format(time.ctime())

t = threading.Thread(name='the_service',target=my_service)
w = threading.Thread(name='the_worker',target=worker)
w2 = threading.Thread(target=worker)
w.start()
w2.start()
t.start()