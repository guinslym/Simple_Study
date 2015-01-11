#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os.path

for parts in [('one','two','three'),
                  ('/','one','two','three'),
                  ('/one','/two','/three'),
                 ]:
    print parts,':',os.path.join(*parts)