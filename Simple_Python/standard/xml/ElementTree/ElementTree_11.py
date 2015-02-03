#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from xml.etree.ElementTree import XML

parsed = XML('''
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

print 'parsed =',parsed
def show_node(node):
    print node.tag
    if node.text is not None and node.text.strip():
        print ' text"%s"' % node.text
    if node.tail is not None and node.tail.strip():
        print ' tail:"%s"' % node.tail
    for name,value in sorted(node.attrib.items()):
        print ' %-4s = "%s"' % (name,value)
    for child in node:
        show_node(child)
    return

for elem in parsed:
    show_node(elem)