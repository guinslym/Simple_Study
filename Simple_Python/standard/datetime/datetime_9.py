#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import datetime

for delta in [
  datetime.timedelta(microseconds=1),
  datetime.timedelta(milliseconds=1),
  datetime.timedelta(seconds=1),
  datetime.timedelta(minutes=1),
  datetime.timedelta(hours=1),
  datetime.timedelta(days=1),
  datetime.timedelta(weeks=1),
]:
    print '%15s = %s seconds' % (delta,delta.total_seconds())