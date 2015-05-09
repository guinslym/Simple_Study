# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:45:54 2015

@author: tim
"""

from twisted.internet import protocol,reactor

class FingerProtocol(protocol.Protocol):
    def connectionMade(self):
        """创建连接的时候"""
        print 'The connection is starting...'
    def dataReceived(self,data):
        """接收到数据的时候"""
        self.transport.write('Server said: '+data)
    def connectionLost(self,reason):
        """连接关闭的时候"""
        reason = 'Finish,and close the connection'
        print reason

class FingerFactory(protocol.Factory):
    protocol = FingerProtocol
    def startFactory(self):
        """开始服务器之前"""
        print 'Starting the server...'
        return
    def stopFactory(self):
        """关闭服务器之前"""
        print 'Stop the server...'
        return

reactor.listenTCP(8000,FingerFactory())
reactor.run()