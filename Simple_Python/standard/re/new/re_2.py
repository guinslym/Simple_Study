#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

# Precompile the patterns
regexes = [re.compile(p) for p in ['this','that']]

text = 'Does this text match the patterns?'
print 'Text:%r\n' % text

for regex in regexes:
    print 'Seeking "%s" -> '% regex.pattern,
    if regex.search(text):
        s = regex.search(text).start()
        e = regex.search(text).end()
        print 'match %s in %d to %d' % (regex.pattern,s,e)
    else:
        print 'no match'