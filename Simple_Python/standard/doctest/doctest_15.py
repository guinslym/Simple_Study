#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import doctest_16

__test__ = {
    'numbers':"""
    >>> my_function(2,3)
    6
    >>> my_function(2.0,3)
    6.0
    """,
    'strings':"""
    >>> my_function('a',3)
    'aaa'
    >>> my_function(3,'a')
    'aaa'
    """,
    'external':doctest_16,
}

def my_function(a,b):
    """Return a * b"""
    return a * b