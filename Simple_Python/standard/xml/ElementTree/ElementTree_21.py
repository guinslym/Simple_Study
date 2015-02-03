#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys
from xml.etree.ElementTree import (Element,
                                                       SubElement,
                                                       ElementTree,)
top = Element('top')
child = SubElement(top,'child')
child.text = 'Contains text.'

empty_child = SubElement(top,'empty_child')

for method in ['xml','html','text']:
    print method
    ElementTree(top).write(sys.stdout,method=method)
    print '\n'