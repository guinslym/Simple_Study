#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from xml.etree import ElementTree

with open('podcasts.opml','rt') as f:
    tree = ElementTree.parse(f)

for node in tree.iter('outline'):
    url = node.attrib.get('xmlUrl')
    if url:
        print url