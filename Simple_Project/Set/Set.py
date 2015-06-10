# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:41:12 2015

@author: tim
"""

class Set(object):
    def __init__(self,value = []):
        self.data = []
        self.concat(value)
    def concat(self,value):
        for x in value:
            if not x in self.data:
                self.data.append(x)
    def intersect(self,other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)
    def fast_interset(self,other):
        res = [x for x in self.data if x in other]
        return Set(res)
    def union(self,other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)
    def __len__(self):
        return len(self.data)
    def __getitem__(self,key):
        return self.data[key]
    def __and__(self,other):
        return self.intersect(other)
    def __or__(self,other):
        return self.union(other)
    def __repr__(self):
        return 'Set'+repr(self.data)