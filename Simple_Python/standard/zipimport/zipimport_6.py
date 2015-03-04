#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')
for name in ['zipimport_4','zipfile_1']:
    print name,importer.is_package(name)