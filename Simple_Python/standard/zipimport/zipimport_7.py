#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
import example

# Find the directory containing the imported package and build the data filename from it.
pkg_dir = os.path.dirname(example.__file__)
data_filename = os.path.join(pkg_dir,'__init__.py')

# Find the prefix of pkg_dir that represents
# the portion of the path that does not need
# to be displayed
dir_prefix = os.path.abspath(os.path.dirname(__file__) or os.getcwd())
if data_filename.startswith(dir_prefix):
    display_filename = data_filename[len(dir_prefix)+1:]
else:
    display_filename = data_filename
# Read the file and show its contents
print display_filename,':'
print open(data_filename,'r').read()