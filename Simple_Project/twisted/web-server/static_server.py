# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:14:24 2015

@author: tim
"""

from twisted.internet import reactor
from twisted.web import static,server

root = static.File('/usr/share/nginx/html')
root.putChild('doc',static.File('/home/tim/share'))
reactor.listenTCP(8000,server.Site(root))
reactor.run()