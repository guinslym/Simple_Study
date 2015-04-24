# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:17:39 2015

@author: tim
"""

from twisted.internet import reactor
from twisted.enterprise import adbapi

dbpool = adbapi.ConnectionPool("sqlite3","users.db",check_same_thread=False)

def _createUserTable(transaction,users):
    transaction.execute("create table users (email text,name text)")
    for email,name in users:
        transaction.execute("insert into users (email,name) values (?,?)",
                            (email,name))
def createUserTable(users):
    return dbpool.runInteraction(_createUserTable,users)
    
def getName(email):
    return dbpool.runQuery("select name from users where email = ?",
                           (email,))

def printResults(results):
    for elt in results:
        print(elt[0])

def finish():
    dbpool.close()
    reactor.stop()
    
users = [('jane@foo.com','jane'),('joe@foo.com','joel')]
d = createUserTable(users)
d.addCallback(lambda x:getName('jane@foo.com'))
d.addCallback(printResults)
reactor.callLater(1,finish)
reactor.run()