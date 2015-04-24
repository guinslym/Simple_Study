#!/usr/bin/env/python
#-*- coding:utf-8 -*-

from twisted.internet import reactor
from twisted.web.static import File
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.util import redirectTo
import os.path
import cgi

class Form(Resource):
    isLeaf = True
    def render_GET(self,request):
        return redirectTo('success',request)
    def render_POST(self,request):
        return '您提交的是:%s' % cgi.escape(request.args['username'][0])
        
#该页面为页面表单
dirname = os.path.dirname(__file__)
root = File(os.path.join(dirname,'form'))
root.putChild('form',Form())
root.putChild('success',File(os.path.join(dirname,'Static/success')))
factory = Site(root)
reactor.listenTCP(8000,factory)
reactor.run()