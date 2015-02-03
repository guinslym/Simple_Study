#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from xml.etree.ElementTree import iterparse
import csv
import sys

writer =csv.writer(sys.stdout,quoting=csv.QUOTE_NONNUMERIC)
group_name = ''

for (event,node) in iterparse('podcasts.opml',events=['start']):
    if node.tag !='outline':
        # Ignore anything not part of the outline
        continue
    if not node.attrib.get('xmlUrl'):
        # Remember the current group
        group_name = node.attrib['text']
    else:
        # Output a podcast entry
        writer.writerow((group_name,node.attrib['text'],
                                  node.attrib['xmlUrl'],
                                  node.attrib.get('htmlUrl'),''
                                  )
                                )