#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import csv
import sys

with open(sys.argv[1],'wt') as f:
    fieldnames = ('Title 1','Title 2','Title 3')
    headers = dict((n,n) for n in fieldnames)

    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writerow(headers)

    for i in range(3):
        writer.writerow({'Title 1':i+1,
                                 'Title 2':chr(ord('a')+i),
                                 'Title 3':'08/%02d/07'%(i+1),
                                 })
print open(sys.argv[1],'rt').read()