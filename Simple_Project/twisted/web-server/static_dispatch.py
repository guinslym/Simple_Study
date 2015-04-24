# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 19:24:36 2015

@author: tim
"""

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

root = File('/usr/share/nginx/html')
root.putChild('about',File('/var/www'))
root.putChild('home',File('/usr/share/nginx/html/site'))
factory = Site(root)
reactor.listenTCP(8000,factory)
reactor.run()