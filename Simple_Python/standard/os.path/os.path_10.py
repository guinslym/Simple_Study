#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os.path
import os

os.chdir('/tmp')
for path in ['.',
                  '..',
                  './one/two/three',
                  '../one/two/three',
                 ]:
    print '%17s :"%s"' % (path,os.path.abspath(path))