#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import collections

c=collections.Counter("abcdgsabxbscsdsba")
for letter in "abcde":
     print "%s:%d" % (letter,c[letter])