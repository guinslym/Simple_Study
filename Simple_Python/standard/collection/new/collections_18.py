#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import collections

print "dict:"
d={}
d["a"]="A"
d["b"]="B"
d["c"]="C"

f={}
f["c"]="C"
f["b"]="B"
f["a"]="A"

print d==f

print "\nOrderedDict:"

d=collections.OrderedDict()
d["a"]="A"
d["b"]="B"
d["c"]="C"
f=collections.OrderedDict()
f["c"]="C"
f["b"]="B"
f["a"]="A"

print d==f