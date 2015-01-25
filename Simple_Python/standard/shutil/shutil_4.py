#! /us/bin/env/python
# -*- coding:utf-8 -*-

from shutil import *
import os
import os.path
import time

def show_file_info(filename):
    stat_info = os.stat(filename)
    print '\tMode :',stat_info.st_mode
    print '\tCreated:',time.ctime(stat_info.st_ctime)
    print '\tAccessed:',time.ctime(stat_info.st_atime)
    print '\tModified:',time.ctime(stat_info.st_mtime)

if not os.path.exists('example'):
    os.mkdir('example')
print 'SOURCE:'
show_file_info(__file__)
copy2(__file__,'example')
print 'DEST:'
show_file_info('example/'+__file__)