#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler

class ErrorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_error(404)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost',8000),ErrorHandler)
    print 'Starting server,use <Ctrl-C> to stop'
    server.serve_forever()