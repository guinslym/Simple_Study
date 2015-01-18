#!/usr/bin/env python
# -*- coding:utf-8 -*-

from re_21 import test_patterns

test_patterns(
    'abbaabbbba',
    [(r'a((a+)|(b+))','a then seq of a or seq of b'),
    (r'a((a|b)+)','a then seq of [ab]'),
    ])