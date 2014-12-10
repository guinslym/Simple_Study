#!/usr/bin/env/python
import urllib2

fd = urllib2.urlopen('http://www.python.org')
print "Retrieved",fd.geturl()
info = fd.info()
for key,value in info.items():
    print "{}={}".format(key,value)