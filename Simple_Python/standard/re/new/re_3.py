#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

text = 'abbaaabbbaaaaa'

pattern = 'ab'
for match in re.findall(pattern,text):
    print 'Found %s' % match
print 'Found "%s at %d times"' % (match,len(match))