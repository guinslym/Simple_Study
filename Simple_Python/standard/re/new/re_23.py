#!/usr/bin/env python
# -*- coding:utf-8 -*-

from re_21 import test_patterns

test_patterns(
    'abbaabbbba',
    [(r'a((a+)|(b+))','capturing form'),
    (r'a((?:a+)|(?:b+))','noncapturing'),
    ])