#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import re

text = 'This is some text -- with punctuation.'
pattern = r'(?i)\bT\w+'
regex = re.compile(pattern)

print 'Text   :',text
print 'Pattern :',pattern
print 'Matches :',regex.findall(text)
