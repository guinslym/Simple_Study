#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import profile
import pstats
from profile_2 import fib,fib_seq

# Read all 5 stats files into a single object
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1,5):
    stats.add('profile_stats_%d.stats' % i)
stats.strip_dirs()

# limit output to lines with "(fib" in them
stats.print_stats('\(fib')