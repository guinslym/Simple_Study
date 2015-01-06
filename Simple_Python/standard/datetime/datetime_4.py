#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import datetime

today = datetime.date.today()
print today
print 'ctime:',today.ctime()
tt = today.timetuple()
print 'tuple :tm_year = ',tt.tm_year
print 'tuple :tm_mon = ',tt.tm_mon
print 'tuple :tm_mday = ',tt.tm_mday
print 'tuple :tm_hour = ',tt.tm_hour
print 'tuple :tm_min = ',tt.tm_min
print 'tuple :tm_sec = ',tt.tm_sec
print 'tuple :tm_wday = ',tt.tm_wday
print 'tuple :tm_yday = ',tt.tm_yday
print 'tuple :tm_isdst = ',tt.tm_isdst
print 'ordinal:',today.toordinal()
print 'Year:',today.year
print 'Mon:',today.month
print 'Day:',today.day