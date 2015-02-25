#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys

class OldStyle:
    pass

class NewStyle(object):
    pass

for obj in [ [],(),{},'c','string',1,2.3,
                 OldStyle,OldStyle(),NewStyle,NewStyle(),
               ]:
    print '%10s :%s' % (type(obj).__name__,sys.getsizeof(obj))