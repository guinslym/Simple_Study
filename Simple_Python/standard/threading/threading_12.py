# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import threading
import logging
import time

logging.basicConfig(
	level=logging.DEBUG,
	format='(%(threadName)-10s) %(message)s',
)

class MyThreadWithArgs(threading.Thread):
	def __init__(self, group = None, target = None,name = None,
		args = (),kwargs = None, verbose = None):
	    threading.Thread.__init__(self,group=group,
	    	                      target=target,
	    	                      name=name,
	    	                      verbose=verbose)
	    self.args = args
	    self.kwargs = kwargs
	    return

	def run(self):
		logging.debug('running with {0} and {1} at {2}'.format(self.args,self.kwargs,time.ctime()))
		return

for x in range(5):
	t = MyThreadWithArgs(args=(x,),kwargs={'a':'Art','b':'Bar','c':'Cat'})
	t.start()