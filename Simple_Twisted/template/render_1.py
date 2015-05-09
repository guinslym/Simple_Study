# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:25:15 2015

@author: tim
"""

from twisted.web.template import flattenString
from element_3 import ExampleElement

def renderDone(output):
    print(output)

flattenString(None,ExampleElement()).addCallback(renderDone)