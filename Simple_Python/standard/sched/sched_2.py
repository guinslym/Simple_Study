#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sched
import time

scheduler = sched.scheduler(time.time,time.sleep)

def long_event(name):
    print 'BEGIN EVENT:',time.ctime(time.time()),name
    time.sleep(2)
    print 'FINISH EVENT:',time.ctime(time.time()),name

print 'START:',time.ctime(time.time())
scheduler.enter(2,1,long_event,('first',))
scheduler.enter(3,1,long_event,('second',))
scheduler.run()