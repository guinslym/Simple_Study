#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import trace
from recurse_1 import recurse

tracer = trace.Trace(count=True,trace=False)
tracer.runfunc(recurse,2)

results = tracer.results()
results.write_results(coverdir='/home/tim/coverdir1')