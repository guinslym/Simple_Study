#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import collections

print "Regular dictionary:"
d={}
d["a"]="A"
d["b"]="B"
d["c"]="C"
for k,v in d.items():
     print k,v

print "\nOrderedDict:"
d=collections.OrderedDict()
d["a"]="A"
d["b"]="B"
d["c"]="C"
for k,v in d.items():
     print k,v