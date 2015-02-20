#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import cgitb
cgitb.enable(format='text',context=12)

class BrokenClass(object):
    """This class has an error."""
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.c = self.a * self.b
        # Really long comment goes here.
        self.d = self.a/self.b
        return
o = BrokenClass(1,0)
