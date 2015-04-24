# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:14:39 2015

@author: tim
"""

from twisted.web.template import Element,renderer,XMLFile
from twisted.python.filepath import FilePath

class ExampleElement(Element):
    loader = XMLFile(FilePath('template-1.xml'))
    
    @renderer
    def header(self,request,tag):
        return tag('Header')
    
    @renderer
    def footer(self,request,tag):
        return tag('Footer.')