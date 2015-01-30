#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import csv
from cStringIO import StringIO
import textwrap

csv.register_dialect('escaped',
                             escapechar='\\',
                             doublequote=False,
                             quoting=csv.QUOTE_NONE,
                             )
csv.register_dialect('singlequote',
                            quotechar="'",
                            quoting=csv.QUOTE_ALL,
                            )
# Generate sample data for all known dialects
samples = []
for name in sorted(csv.list_dialects()):
    buffer = StringIO()
    dialect = csv.get_dialect(name)
    writer = csv.writer(buffer,dialect=dialect)
    writer.writerow(
        ('coll',1,'10/01/2010',
         'Special chars "\' %s to parse' % dialect.delimiter)
        )
    samples.append((name,dialect,buffer.getvalue()))
# Guess the dialect for a given sample,and then use the results to parse the data
sniffer =csv.Sniffer()
for name,expected,sample in samples:
    print 'Dialect: "%s"\n' %name
    dialect = sniffer.sniff(sample,delimiters=',\t')
    reader = csv.reader(StringIO(sample),dialect=dialect)
    print reader.next()
    print