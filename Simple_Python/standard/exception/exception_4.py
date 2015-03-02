#! /usr/bin/env/python
# -*- coding:utf-8 -*-

class MyClass(object):
    @property
    def attribute(self):
        return 'This is the attribute value'
o = MyClass()
print o.attribute
o.attribute = 'New value'