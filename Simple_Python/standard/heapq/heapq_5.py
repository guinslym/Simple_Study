#! /usr/bin/env/python
# -*- coding:utf-8 -*

import heapq
from heapq_1 import show_tree
from heapq_3 import data

print 'random   :',data
heapq.heapify(data)
print 'heapified:'
show_tree(data)
print

for i in xrange(2):
    smallest = heapq.heappop(data)
    print 'pop    %3d' % smallest
    show_tree(data)