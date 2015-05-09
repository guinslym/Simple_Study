# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from twisted.internet import reactor
from twisted.web.client import downloadPage
import sys

def printError(failure):
    print >>sys.stderr,failure
    
def stop(result):
    reactor.stop()

if len(sys.argv) !=3:
    print >>sys.stderr,'usage:python download_resource.py <url> <output file>'
    sys.exit(1)
    
d = downloadPage(sys.argv[1],sys.argv[2])
d.addErrback(printError)
d.addBoth(stop)
reactor.run()