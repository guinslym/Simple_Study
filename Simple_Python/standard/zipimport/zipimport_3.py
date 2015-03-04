#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')
code = importer.get_code('zipfile_1')
print code