#!/usr/bin/env/python
#-*- coding:utf-8 -*-

def binary_search(data,target,num=False):
    data_length = len(data)-1
    head = 0
    num  = 0
    if data_length==1:
        if target in data:
            return 0
        else:
            return -1
    data.sort()
    while head<=data_length:
        mid = (head&data_length)+((head^data_length)>>1)
        if data[mid]==target:
            if num:
                print num
            return mid
        elif data[mid] > target:
            data_length = mid - 1
        else:
           head = mid +1
        num +=1
    return -1

data=[1,0,2,85,45,13,29,3,30]
print(binary_search(data,29,True))