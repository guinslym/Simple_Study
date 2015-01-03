#! /usr/bin/env/python
# -*- coding:utf-8 -*

from itertools import *

values = [(0,5),(1,6),(2,7),(3,8),(4,9)]
for i in starmap(lambda x,y:(x,y,x*9),values):
    print '%d * %d = %d' % i