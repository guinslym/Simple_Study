#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import multiprocessing

def producer(ns,event):
    ns.value = 'This is the value'
    event.set()

def consumer(ns,event):
    try:
        value = ns.value
    except Exception, e:
        print 'Before event,error:',str(e)
    event.wait()
    print 'After event:',ns.value

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    event = multiprocessing.Event()
    p = multiprocessing.Process(target=producer,
                                               args=(namespace,event))
    c = multiprocessing.Process(target=consumer,
                                               args=(namespace,event))
    c.start()
    p.start()
    c.join()
    p.join()