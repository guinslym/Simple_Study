#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import hashlib
from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem)
print h.hexdigest()