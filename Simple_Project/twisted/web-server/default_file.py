# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:41:27 2015

@author: tim
"""

from twisted.application import internet,service
from twisted.web import static,server,script
from twisted.python import log
import sys

root = static.File('/home/tim/default')
root.indexNames = ['index.rpy','index.html']
root.processors = {'rpy':script.ResourceScript}
log.startLogging(sys.stdout)
application = service.Application('web')
sc = service.IServiceCollection(application)
site = server.Site(root)
i = internet.TCPServer(8000,site)
i.setServiceParent(sc)