#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys
import threading
from Queue import Queue
import time

def show_thread(q,extraByteCodes):
    for i in range(5):
        for j in range(extraByteCodes):
            pass
        q.put(threading.current_thread().name)
    return

def run_thread(prefix,interval,extraByteCodes):
    print '%s interval = %s with %s extra operations' % (prefix,interval,extraByteCodes)
    sys.setcheckinterval(interval)
    q = Queue()
    threads = [ threading.Thread(target=show_thread,
                                                 name='%s T%s' % (prefix,i),
                                                 args=(q,extraByteCodes)
                                                 )
                             for i in range(3)
                    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    while not q.empty():
        print q.get()
    print
    return

run_thread('Default',interval=10,extraByteCodes=1000)
run_thread('Custom',interval=10,extraByteCodes=0)