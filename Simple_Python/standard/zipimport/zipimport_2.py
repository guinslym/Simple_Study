#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')

for module_name in ['index.html','not_there','zipfile_1']:
    print module_name,':',importer.find_module(module_name)