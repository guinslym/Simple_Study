#! /usr/bin/env/python
# -*- coding:utf-8 -*

import heapq
from heapq_1 import show_tree
from heapq_3 import data

print 'random     :',data
heapq.heapify(data)
print 'heapified  :'
show_tree(data)