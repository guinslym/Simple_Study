# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:47:27 2015

@author: tim
"""

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import sqlite3

from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/(\w+)",WorkHandler)]
        tornado.web.Application.__init__(self,handlers,debug=True)
        
class WorkHandler(tornado.web.RequestHandler):
    def get(self,word):
        conn = sqlite3.connect('book.db')
        curs = conn.cursor()
        curs.execute('select * from book where _rowid_ =?',word)
        word_doc=curs.fetchone()
        if word_doc:
            self.write(word_doc[0]+'\n')
        else:
            self.set_status(404)
            self.write({"error":"Word not found"})
    def post(self,word):
        definition = self.get_argument('name')
        conn = sqlite3.connect('book.db')
        curs = conn.cursor()
        curs.execute('select * from book where _rowid_ =?',word)
        word_doc=curs.fetchone()
        if word_doc:
            curs.execute('update book set name = ?',word_doc[0])
        else:
            curs.insert('insert into book values(?,?)',[(definition,10000)])
        curs.commit()
        self.write(word_doc)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()