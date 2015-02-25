#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys

class LineCounter(object):
    def __init__(self):
        self.count = 0
    def __str__(self):
        self.count +=1
        return '(%3d)> '%self.count