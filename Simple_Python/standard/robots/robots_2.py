#! /usr/bin/env/python
# -*- coding:utf-8 -*

import robotparser
import time
import urlparse

AGENT_NAME = 'PyMOTW'
parser = robotparser.RobotFileParser()
#Using the local copy
parser.set_url('http://www.jd.com/robots.txt')
parser.read()
parser.modified()

PATHS = [
   '/',
   '/pinpai/',
   '/help/',
   '/admin/',
]

for path in PATHS:
    age = int(time.time() - parser.mtime())
    print 'age:',age,
    if age > 1:
    	print 'rereading robots.txt'
    	parser.read()
    	parser.modified()
    else:
    	print
    print '%6s:%s' % (parser.can_fetch(AGENT_NAME,path),path)
    #Simulate a delay in processing
    time.sleep(1)
    print