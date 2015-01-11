#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import subprocess

try:
    subprocess.check_call(['false'])
except subprocess.CalledProcessError as err:
    print 'ERROR:',err