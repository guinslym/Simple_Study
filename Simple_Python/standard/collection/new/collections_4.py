#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import collections

c=collections.Counter("extremely")
c["z"]=1
print c
print list(c.elements())