# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:26:41 2015

@author: tim
"""

from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.server import Site

import cgi

class FormPage(Resource):
    isLeaf = True
    def render_GET(self,request):
        template = """
        <html>
        <body>
        <form method="POST">
          <input name="form-field" type="text" />
          <input type="submit" />
        </form>
        </body>
        </html>
        """
        return template
    def render_POST(self,request):
        render = """
        <html>
        <body>You submitted:%s</body>
        </html>
        """
        return render % cgi.escape(request.args["form-field"][0])
        
resource = FormPage()
factory = Site(resource)
reactor.listenTCP(8000,factory)
reactor.run()