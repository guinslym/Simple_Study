# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 06:34:46 2015

@author: tim
"""

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

import time

class BusyPage(Resource):
    isLeaf = True
    def render_GET(self,request):
        time.sleep(5)
        return 'Finally done,at %s' % (time.asctime(),)

resource = BusyPage()
factory = Site(resource)
reactor.listenTCP(8000,factory)
reactor.run()