# -*- coding:utf-8 -*-
#！/usr/bin/env/python

import threading,time

def worker(num):
	"""thread worker function"""
	print 'worker:{0},the number is {1}'.format(time.ctime(),num)
	return

threads = []
for x in range(5):
	t = threading.Thread(target=worker,args=(x,))
	time.sleep(1)
	threads.append(t)
	t.start()