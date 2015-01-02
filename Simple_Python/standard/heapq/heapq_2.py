#! /usr/bin/env/python
# -*- coding:utf-8 -*

import heapq
from heapq_1 import show_tree
from heapq_3 import data

heap = []
print 'random:',data
print

for n in data:
    print 'add %3d:' % n
    heapq.heappush(heap,n)
    show_tree(heap)