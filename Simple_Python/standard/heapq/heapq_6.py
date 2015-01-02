#! /usr/bin/env/python
# -*- coding:utf-8 -*

import heapq
from heapq_1 import show_tree
from heapq_3 import data

heapq.heapify(data)
print 'start:'
show_tree(data)

for n in [0,13]:
    smallest = heapq.heapreplace(data,n)
    print 'replace %2d with %2d:' % (smallest,n)
    show_tree(data)