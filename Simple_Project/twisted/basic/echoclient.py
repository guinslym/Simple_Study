# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 06:12:29 2015

@author: tim
"""

from twisted.internet import reactor,protocol
import time

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(time.ctime())
    def dataReceived(self,data):
        print "Server said:",data
        self.transport.loseConnection() #断开与服务器的连接

class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self,addr):
        return EchoClient()
    def clientConnectionFailed(self,connector,reason):
        print "Connection Failed"
        reactor.stop()
    def clientConnectionLost(self,connector,reason):
        print "connection lost"
        reactor.stop()
        
reactor.connectTCP("localhost",8000,EchoFactory())
reactor.run()