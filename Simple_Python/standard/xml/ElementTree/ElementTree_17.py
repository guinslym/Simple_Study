#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from xml.etree.ElementTree import Element,tostring
from ElementTree_14 import prettify

top = Element('top')
children = [
             Element('child',num=str(i))
             for i in range(3)
            ]
top.extend(children)
print prettify(top)