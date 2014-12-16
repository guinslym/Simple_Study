# -*- coding:utf-8 -*-
#！/usr/bin/env/python

import threading
import time

def worker():
	"""thread worker function"""
	print 'Work on {0}'.format(time.ctime())
	return

threads = []
for x in range(5):
	t = threading.Thread(target=worker)
	time.sleep(1)
	threads.append(t)
	t.start()