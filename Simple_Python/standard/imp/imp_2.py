#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imp
from imp_1 import module_types
import os

# Get the full name of the directory containing this module
base_dir = os.path.dirname(__file__) or os.getcwd()

print 'Package:'
f,pkg_fname,description = imp.find_module('example')
print module_types[description[2]],pkg_fname.replace(base_dir,'.')
print
print 'Submodule:'
f,mod_fname,description = imp.find_module('submodule',[pkg_fname])
print module_types[description[2]],mod_fname.replace(base_dir,'.')
if f:f.close()