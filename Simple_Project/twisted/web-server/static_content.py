# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:59:11 2015

@author: tim
"""

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

resource = File("/usr/share/nginx/html")
factory = Site(resource)
reactor.listenTCP(8000,factory)
reactor.run()