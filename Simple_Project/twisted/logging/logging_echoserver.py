# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 07:20:01 2015

@author: tim
"""

from twisted.internet import reactor,protocol
from twisted.python import log

class Echo(protocol.Protocol):
    def dataReceived(self,data):
        log.msg(data)
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self,addr):
        return Echo()
        
log.startLogging(open('echo.log','w'))
reactor.listenTCP(8000,EchoFactory())
reactor.run()