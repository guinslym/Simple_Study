# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:23:34 2015

@author: tim
"""

import datetime

class Date(object):
    def __init__(self):
        self.date = datetime.date
    def getToday(self):
        """获取今天的日期"""
        return self.date.today().__str__()
    def getDate(self,ordinal):
        """获取指定间隔的日期"""
        self.min_num = self.date(1900,1,1).toordinal()
        self.max_num = self.date.max.toordinal()
        if ordinal in range(self.min_num,self.max_num):
            d = self.date.fromordinal(ordinal)
            return self._format_date(d)
        else:
            if ordinal < self.min_num:
                raise Exception('The given number %s is smaller than %s' % (ordinal,self.min_num))
            else:
                raise Exception('The given number %s is greater than %s' % (ordinal,self.max_num))
    def _format_date(self,d,format="%Y-%m-%d"):
        """格式化日期"""
        return d.__format__(format)
    def getDateFromTimestamp(self,timestamp):
        """获取指定时间戳的日期"""
        d = self.date.fromtimestamp(timestamp)
        return self._format_date(d)
        
d = Date()
print d.getToday()
print d.getDate(1100000)
print d.getDateFromTimestamp(13000000000)