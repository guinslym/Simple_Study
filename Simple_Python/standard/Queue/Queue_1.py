#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import Queue

q = Queue.Queue()

for i in range(10):
    q.put(i)

while not q.empty():
    print q.get(),
print