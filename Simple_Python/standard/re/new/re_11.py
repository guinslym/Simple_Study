#!/usr/bin/env python
# -*- coding:utf-8 -*-

from re_5 import test_pattern

test_pattern(
    'abbaabbba',
    [('a,','a followed by any one character'),
     ('b.','b followed by any one character'),
     ('a.*b','a followed by anything,ending in b'),
     ('a.*?b','a followed by anything,ending in b'),
    ])