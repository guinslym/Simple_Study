#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import cProfile as profile
import pstats
from profile_2 import fib,fib_seq

# Read all 5 stats files into a single object
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1,5):
    stats.add('profile_stats_%d.stats' % i)
stats.strip_dirs()
stats.sort_stats('cumulative')

print 'INCOMING CALLERS:'
stats.print_callers('\(fib')

print 'OUTGOING CALLERS:'
stats.print_callees('\(fib')