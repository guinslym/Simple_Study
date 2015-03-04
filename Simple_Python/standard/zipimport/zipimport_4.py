#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')
module = importer.load_module('zipfile_1')
print 'Name   :',module.__name__
print 'Loader :',module.__loader__
print 'Zipfile    :',module.zipfile