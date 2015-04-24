# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:32:29 2015

@author: tim
"""

from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
import time

class PaymentRequest(Resource):
    def render_GET(self,request):
        request.setResponseCode(200)
        return '<h1>Hello world,%s</h1>' % time.asctime()
class Home(Resource):
    isLeaf = True
    def render_GET(self,request):
        return '<h1>Nice to meet you!</h1>'

root = Home()
root.putChild('buy',PaymentRequest())
factory = Site(root)
reactor.listenTCP(8000,factory)
reactor.run()