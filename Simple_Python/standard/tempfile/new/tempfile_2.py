#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write('some data')
    temp.seek(0)

    print temp.read()