#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import shelve
from contextlib import closing
with closing(shelve.open('test_shelf.db')) as s:
    s['key1'] = {'int':10,'float':9.5,'string':'Sample data'}