#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import gzip
import os
import itertools

with gzip.open('example_lines.txt.gz','wb') as output:
    output.writelines(
        itertools.repeat('This same line,over and over.\n',10)
        )
os.system('gunzip example_lines.txt.gz')
os.system('cat example_lines.txt')