#!/usr/bin/env/python
#-*- coding:utf-8 -*-

from twisted.internet import reactor
from twisted.web.static import File
from twisted.web.server import Site
import os.path

#该页面为404页面
dirname = os.path.dirname(__file__)
root = File(os.path.join(dirname,'Static/404'))
factory = Site(root)
reactor.listenTCP(8000,factory)
reactor.run()