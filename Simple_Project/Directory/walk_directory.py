# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:14:57 2015
遍历目录树
@author: tim
"""
from __future__ import print_function
from __future__ import division
import sys
import os
import time

def walk_directory(dir,sep='-'):
    """遍历指定的文件目录"""
    for dirname,subname,filename in os.walk(dir):
        print('\r')
        print(dirname)
        print(sep*30)
        for fname in filename:
            file_name = os.path.join(dirname,fname)
            print(file_name,get_print_pretty(file_name))
            #print(get_file_permission(file_name))
            #print(get_file_mtime(file_name))
            
def get_print_pretty(filename):
    """输出人性化的文件大小"""
    filesize = os.path.getsize(filename)
    output_format = '{:.2f}'
    if (filesize>>9)<=1:
        file_size = output_format.format(filesize)+'B'
    elif (filesize>>19)<=1:
        file_size = output_format.format(filesize/10**3)+'KB'
    elif (filesize>>29)<=1:
        file_size = output_format.format(filesize/10**6)+'MB'
    elif (filesize>>39)<=1:
        file_size = output_format.format(filesize/10**9)+'GB'
    else:
        file_size = 'too many'
    return file_size

def get_binary_size(filename):
    """获取系统内部文件大小"""
    filesize = os.path.getsize(filename)
    output_format = '{:.2f}'
    if (filesize>>9)<=1:
        file_size = output_format.format(filesize)+'B'
    elif (filesize>>19)<=1:
        file_size = output_format.format(filesize>>10)+'KB'
    elif (filesize>>29)<=1:
        file_size = output_format.format(filesize>>20)+'MB'
    elif (filesize>>39)<=1:
        file_size = output_format.format(filesize>>30)+'GB'
    else:
        file_size = 'too many'
    return file_size

def get_file_permission(filename):
    """获取文件的权限"""
    bits = os.stat(filename).st_mode
    return oct(bits)[4:]
def get_file_mtime(filename):
    """获取文件修改时间"""
    mtime = os.path.getmtime(filename)
    modify_time = get_pretty_time(mtime)
    return modify_time

def get_pretty_time(format_time):
    """输出人性化的时间"""
    t = time.localtime(format_time)
    time_info = time.strftime('%Y-%m-%d %H:%M:%S',t)
    return time_info

if __name__ == '__main__':
    directory = sys.argv[1]
    walk_directory(directory)