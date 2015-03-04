#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import pkgutil
import pprint

print 'demopkg.__path__ before:'
pprint.pprint(__path__)
print

__path__ = pkgutil.extend_path(__path__,__name__)
print 'demopkg.__path__ after:'
pprint.pprint(__path__)
print