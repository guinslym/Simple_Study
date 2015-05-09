# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:42:55 2015

@author: tim
"""

from twisted.application import internet,service
from twisted.web import static,server

root = static.File('/usr/share/nginx/html')
application = service.Application('web')
site = server.Site(root)
sc = service.IServiceCollection(application)
i = internet.TCPServer(8000,site)
i.setServiceParent(sc)