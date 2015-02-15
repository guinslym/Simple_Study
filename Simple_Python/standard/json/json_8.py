#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import json
import json_7

obj = json_7.MyObj('instance value goes here')

print 'First attempt'
try:
    print json.dumps(obj)
except TypeError, err:
    print 'ERROR:',err

def convert_to_bulitin_type(obj):
    print 'Default(',repr(obj),')'
    # Convert objects to a dictionary of their representation
    d = {'__class__':obj.__class__.__name__,
           '__module__':obj.__module__,
          }
    d.update(obj.__dict__)
    return d
print
print 'With default'
print json.dumps(obj,default=convert_to_bulitin_type)