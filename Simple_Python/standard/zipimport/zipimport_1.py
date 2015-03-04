#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys
import zipfile

if __name__ == '__main__':
    zf = zipfile.PyZipFile('zipimport_example.zip',mode='w')
    try:
        zf.writepy('.')
        zf.write('wx_sample.php')
        zf.write('index.html')
    finally:
        zf.close()
    for name in zf.namelist():
        print name