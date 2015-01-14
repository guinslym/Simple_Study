#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os

dir_name = 'os_directories_example'

print 'Creating',dir_name
os.makedirs(dir_name)

file_name = os.path.join(dir_name,'example.txt')
print 'Creating',file_name
with open(file_name,'wt') as f:
    f.write('example file')

print 'Listing',dir_name
print os.listdir(dir_name)

print 'Cleaning up'
os.unlink(file_name)
os.rmdir(dir_name)