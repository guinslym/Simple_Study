#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import hashlib
from hashlib_data import lorem

h = hashlib.sha1()
h.update(lorem)
print h.hexdigest()