#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from xml.etree.ElementTree import XMLID

tree,id_map = XMLID('''
    <root>
      <group>
      <child id="a">This is a child "a".</child>
      <child id="b">This is a child "b".</child>
      </group>
      <group>
      <child id="c">This is a child "c".</child>
      </group>
    </root>
    ''')

for key,value in sorted(id_map.items()):
    print '%s = %s' % (key,value)