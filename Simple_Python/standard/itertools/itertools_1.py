#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from itertools import *

for i in chain([1,2,3],['a','b','c']):
    print i,
print