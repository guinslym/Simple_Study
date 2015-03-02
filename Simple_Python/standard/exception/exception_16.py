#! /usr/bin/env/python
# -*- coding:utf-8 -*-

class BaseClass(object):
    """Defines the interface"""
    def __init__(self):
        super(BaseClass,self).__init__()
    def do_something(self):
        """The interface,not implemented"""
        raise NotImplementedError(
                 self.__class__.__name__+'do_something'
                 )
class Subclass(BaseClass):
    """implementes the interface"""
    def do_something(self):
        """really does something"""
        print self.__class__.__name__+'doing something!'

Subclass().do_something()
BaseClass().do_something()