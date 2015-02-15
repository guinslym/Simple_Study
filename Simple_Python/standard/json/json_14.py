#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import json
from StringIO import StringIO

f = StringIO('[{"a":"张三","b":[2,4],"c":3.0}]')
print json.load(f)