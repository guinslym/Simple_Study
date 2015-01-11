#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os.path
for path in ['/filename.txt',
                  '/filename',
                  '/path/to/filename.txt',
                  '/',
                  '',
                  'my-archive.tar.gz',
                  'no-extension.',]:
    print '%21s : ' % path,os.path.splitext(path)