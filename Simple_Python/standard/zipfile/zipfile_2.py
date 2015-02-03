#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import zipfile

with zipfile.ZipFile("test.zip","r") as zf:
    print zf.namelist()