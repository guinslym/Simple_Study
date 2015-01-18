#!/usr/bin/env python
# -*- coding:utf-8 -*-

from re_5 import test_pattern

test_pattern(
    'abbaaabbbaaaaa',
    [('a(ab)','a followed by literal ab'),
    ('a(a*b*)','a followed by 0-n a and 0-n b'),
    ('a(ab)*','a followed by 0-n ab'),
    ('a(ab)+','a followed by 1-n ab'),
    ])