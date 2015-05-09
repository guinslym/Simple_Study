# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:28:34 2015

@author: tim
"""

import time

class Time(object):
    def getgmttime(self,secs=None):
        """获取格林时间"""
        if secs is None:
            gmt=time.gmtime()
        else:
            gmt=time.gmtime(secs)
        return self._format_time(gmt)
    def _format_time(self,gmt,time_format="%Y-%m-%d %H:%M:%S"):
        """格式化时间"""
        return time.strftime(time_format,gmt)
    def getcmtime(self,secs=None):
        if secs is None:
            cmt = time.ctime()
        else:
            cmt = time.ctime(secs)
        return cmt
    def getlocaltime(self,secs=None):
        """获取当前时间"""
        if secs is None:
            local = time.localtime()
        else:
            local = time.localtime(secs)
        return self._format_time(local)
    def getgmttimestamp(self):
        """获取格林时间戳"""
        t = time.gmtime()
        return self._tupleToTimestamp(t)
    def gettimestamp(self):
        """获取当前时间戳"""
        t = time.localtime()
        return self._tupleToTimestamp(t)
    def _tupleToTimestamp(self,t):
        """时间元组转换为时间戳"""
        return int(time.mktime(t))
    def getfloattimestamp(self):
        """获取浮点的时间戳"""
        return time.time()
          
#t = Time()
#print t.getgmttime()
#print t.getlocaltime()
#print t.gettimestamp()
#print t.getgmttimestamp()
if __name__ == '__main__':
    Time()