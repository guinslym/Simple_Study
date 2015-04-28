# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 09:16:39 2015

@author: tim
"""

class BinarySearch(object):
    def BinarySearch(self,data,target):
        self._handle(data)
        start = 0
        list_len = len(data)-1
        while(start<=list_len):
            mid = (start+list_len)/2
            if target < data[mid]:
                list_len = mid
            elif target > data[mid]:
                start = mid
            else:
                return mid
        return -1
    def _handle(self,data):
        data.sort()
        
b = BinarySearch()
data = [1,34,12,45,6,9,22,12,33]
print b.BinarySearch(data,12)