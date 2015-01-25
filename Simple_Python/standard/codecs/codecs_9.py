#! /us/bin/env/python
# -*- coding:utf-8 -*-

import codecs
import sys

error_handling = sys.argv[1]

text = u'pi:\u03c0'

try:
    # Save the data,encoded as ASCII,using the error
    # Handling mode specified on the command line.
    with codecs.open('encode_error.txt','w',
                               encoding='ascii',
                               errors=error_handling) as f:
        f.write(text)
except UnicodeEncodeError, e:
    print 'ERROR:',e
else:
    # If there was no error writing to the file,
    # show what it contains.
    with open('encode_error.txt','rb') as f:
        print 'File contents:',repr(f.read())