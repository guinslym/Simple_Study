#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import json
import json_7

class MyEncoder(json.JSONEncoder):
    def default(self,obj):
        print 'default(',repr(obj),')'
        # Convert objects to a dictionary of their representation
        d = {'__class__':obj.__class__.__name__,
               '__module__':obj.__module__,
              }
        d.update(obj.__dict__)
        return d
obj = json_7.MyObj('internal data')
print obj
print MyEncoder().encode(obj)