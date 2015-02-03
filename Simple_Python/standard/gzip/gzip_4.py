#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import gzip
with gzip.open('example.txt.gz','rb') as input_file:
    print input_file.read()