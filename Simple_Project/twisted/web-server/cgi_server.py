# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:21:51 2015

@author: tim
"""

from twisted.internet import reactor
from twisted.web import static,server,twcgi

root = static.File('/usr/share/nginx/html')
root.putChild('cgi-bin',twcgi.CGIDirectory('/home/tim/cgi-bin'))
reactor.listenTCP(8000,server.Site(root))
reactor.run()