# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 07:29:13 2015

@author: tim
"""

from twisted.internet import reactor
from twisted.web.resource import Resource,NoResource
from twisted.web.server import Site
from calendar import LocaleHTMLCalendar

class YearPage(Resource):
    def __init__(self,year):
        Resource.__init__(self)
        self.year = year
    
    def render_GET(self,request):
        d = LocaleHTMLCalendar()
        return "%s" % d.formatyearpage(self.year,2,encoding='utf-8')
class CalendarHome(Resource):
    def getChild(self,name,request):
        if name == '':
            return self
        if name.isdigit():
            return YearPage(int(name))
        else:
            return NoResource()
    def render_GET(self,request):
        return "<html><body>Welcome to calendar world</body></html>"
        
root = CalendarHome()
factory = Site(root)
    
reactor.listenTCP(8000,factory)
reactor.run()