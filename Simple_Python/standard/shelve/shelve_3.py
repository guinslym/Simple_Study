#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import shelve
from contextlib import closing
with closing(shelve.open('test_shelf.db',flag='r')) as s:
    existing = s['key1']
print existing