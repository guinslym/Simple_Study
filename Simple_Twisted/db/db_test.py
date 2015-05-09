# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 08:38:33 2015

@author: tim
"""

from twisted.internet import reactor
from twisted.enterprise import adbapi

dbpool = adbapi.ConnectionPool("psycopg2","dbname=tim user=tim")

def getName(email):
    return dbpool.runQuery("select name from user where email=?",(email,))

def printResults(results):
    for elt in results:
        print(elt[0])

def finish():
    dbpool.close()
    reactor.stop()

d = getName('z@126.com')
d.addCallback(printResults)

reactor.callLater(1,finish)
reactor.run()