#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import trace
from recurse_1 import recurse

tracer = trace.Trace(count=False,trace=True)
tracer.run('recurse(2)')