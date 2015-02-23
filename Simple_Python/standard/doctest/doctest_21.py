#! /usr/bin/env/python
# -*- coding:utf-8 -*

class TestGlobals(object):
    def one(self):
        """
        >>> var = 'value'
        >>> 'var' in globals()
        True
        """
    def two(self):
        """
        >>> 'var' in globals()
        False
        """
