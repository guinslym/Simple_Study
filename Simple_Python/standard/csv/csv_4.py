#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import csv
csv.register_dialect('pipes',delimiter='/')

with open('output.csv','r') as f:
    reader = csv.reader(f,dialect='pipes')
    for row in reader:
        print row