#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import linecache

#Errors are even hidden if linecache cannot find the file
no_such_file = linecache.getline('this_file_does_not_exist.txt',1)
print 'NO FILE:%r' % no_such_file