#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')
for module_name in ['zipfile_1','zipimport_4']:
    source = importer.get_source(module_name)
    print '='*80
    print module_name
    print '='*80
    print source
    print