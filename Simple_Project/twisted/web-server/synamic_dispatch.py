# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:30:40 2015

@author: tim
"""

from twisted.internet import reactor
from twisted.web.resource import Resource,NoResource
from twisted.web.util import redirectTo
from twisted.web.server import Site

from datetime import datetime
from calendar import HTMLCalendar

class YearPage(Resource):
    def __init__(self,year):
        Resource.__init__(self)
        self.year = year
    def render_GET(self,request):
        cal = HTMLCalendar()
        return cal.formatyear(self.year,2)
        
class CalendarHome(Resource):
    def getChild(self,name,request):
        if name == "":
            return self
        if name.isdigit():
            return YearPage(int(name))
        else:
            return NoResource()
    def render_GET(self,content):
        return redirectTo(datetime.now().year,content)
        #return "<html><body><h1>Welcome to calendar server!</h1></body></html>"

resource = CalendarHome()          
factory = Site(resource)
reactor.listenTCP(8000,factory)
reactor.run()