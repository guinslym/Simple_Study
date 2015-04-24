# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:49:13 2015

@author: tim
"""

from twisted.internet import reactor
from twisted.web import http

class MyRequestHandler(http.Request):
    resource = {
      '/':"<h1>Hello world!</h1>",
      '/about':"<h1>About US</h1>"
    }
    def process(self):
        self.setHeader('Content-Type','text/html')
        if self.resource.has_key(self.path):
            self.write(self.resource[self.path])
        else:
            self.setResponseCode(http.NOT_FOUND)
            self.write('<h1>Not Found!404</h1>')
        self.finish()

class MyHTTP(http.HTTPChannel):
    requestFactory = MyRequestHandler

class MyHTTPFactory(http.HTTPFactory):
    def buildProtocol(self,addr):
        return MyHTTP()

reactor.listenTCP(8000,MyHTTPFactory())
reactor.run()