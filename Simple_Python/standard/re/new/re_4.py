#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

text = 'abbaaabbbaaaaa'

pattern = 'ab'
for match in re.finditer(pattern,text):
    s = match.start()
    e = match.end()
    print 'Found "%s" at %d:%d' % (text[s:e],s,e)