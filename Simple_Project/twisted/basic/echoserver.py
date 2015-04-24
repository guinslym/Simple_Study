# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 06:08:00 2015

@author: tim
"""

from twisted.internet import protocol,reactor

class Echo(protocol.Protocol):
    def dataReceived(self,data):
        self.transport.write(data)
        
class EchoFactory(protocol.Factory):
    def buildProtocol(self,addr):
        return Echo()
        
reactor.listenTCP(8000,EchoFactory())
reactor.run()