# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 07:10:30 2015

@author: tim
"""

from twisted.internet import reactor
from twisted.web.client import getPage

import sys

def printPage(result):
    print(result)
    
def printError(failure):
    print >>sys.stderr,failure
    
def stop(result):
    reactor.stop()
    
if len(sys.argv)!=2:
    print >>sys.stderr,'Usage:python print_resource.py</url>'
    exit(1)

d = getPage(sys.argv[1])
d.addCallbacks(printPage,printError)
d.addBoth(stop)
reactor.run()