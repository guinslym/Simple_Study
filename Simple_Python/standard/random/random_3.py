#! /us/bin/env/python
# -*- coding:utf-8 -*-

import random

random.seed(1)
for i in xrange(5):
    print '%04.3f' % random.random(),
print