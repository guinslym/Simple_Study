#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sched
import time
scheduler = sched.scheduler(time.time,time.sleep)

def print_event(name,start):
    now = time.time()
    elapsed = int(now-start)
    print 'EVENT:%s elapsed=%s name=%s' % (time.ctime(now),
                                                                      elapsed,
                                                                      name)
start = time.time()
print 'START:',time.ctime(start)
scheduler.enter(2,1,print_event,('first',start))
scheduler.enter(3,1,print_event,('second',start))
scheduler.run()