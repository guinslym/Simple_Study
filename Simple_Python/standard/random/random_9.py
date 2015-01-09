#! /us/bin/env/python
# -*- coding:utf-8 -*-

import random

with open('/home/tim/webservice','rt') as f:
    words = f.readlines()
words = [w.rstrip() for w in words]

for w in random.sample(words,5):
    print w