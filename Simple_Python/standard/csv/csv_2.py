#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

with open(sys.argv[1],'wt') as f:
    writer = csv.writer(f)
    writer.writerow((u'名称',u'性别',u'年龄'))
    for i in range(3):
        writer.writerow((i+1,
                                chr(ord('a')+i),
                                '/08/%2d/07' % (i+1),
                                ))
print open(sys.argv[1],'rt').read()