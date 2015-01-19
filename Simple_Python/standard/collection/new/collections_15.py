#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import collections

try:
    collections.namedtuple('Person','name class age gender')
except ValueError, err:
    print err

try:
    collections.namedtuple('Person','name age gender age')
except ValueError, err:
    print err