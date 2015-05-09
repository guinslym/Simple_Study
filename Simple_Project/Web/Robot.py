# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:40:48 2015

@author: tim
"""
import robotparser
from Time import Time 

class Robot(object):
    def __init__(self):
        self.rp = robotparser.RobotFileParser()
    def Can_fetch(self,**kargs):
        """查看是否可以爬取指定页面下的内容"""
        self.url = kargs['url']
        self.robots_file = self.url+ '/robots.txt'
        self.fetch = kargs['fetch']
        self.rp.set_url(self.robots_file)
        self.rp.read()
        for x in self.fetch:
            print self.rp.can_fetch(self.fetch[x],self.url+'/'+x)
    def get_mtime(self):
        t = Time()
        return t.getgmttime(self.rp.mtime())
    def get_modified(self):
        return Time.getgmttime(self.rp.modified())
        
if __name__ == '__main__':
    r = Robot()
    r.Can_fetch(url='http://www.jd.com',
                  fetch={
                  'pinpai/*.html':'*',
                  'pop/*.html':'*'
                  })
    print r.get_mtime()