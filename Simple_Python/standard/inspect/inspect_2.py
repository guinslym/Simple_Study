#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import inspect
import example

for name,data in inspect.getmembers(example):
    if name.startswith('__'):
        continue
    print '%s:%r' % (name,data)