#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import filecmp

filecmp.dircmp('example/dir1','example/dir2').report_full_closure()