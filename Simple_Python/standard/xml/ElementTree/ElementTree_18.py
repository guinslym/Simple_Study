#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from xml.etree.ElementTree import Element,tostring,SubElement,XML
from ElementTree_14 import prettify

top = Element('top')

parent = SubElement(top,'parent')
children = XML(
    '<root><child num="0" /><child num="1" /><child num="2" /></root>')
parent.extend(children)
print prettify(top)