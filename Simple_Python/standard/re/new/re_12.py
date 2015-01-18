#!/usr/bin/env python
# -*- coding:utf-8 -*-

from re_5 import test_pattern

test_pattern(
    'A prime #1 example',
    [(r'\d+,','sequence of digits'),
     (r'\D+','sequence of nondigits'),
     (r'\s+','sequence of whitespace'),
     (r'\S+','sequence of nonwhitespace'),
     (r'\w+','alphanumeric characters'),
     (r'\W+','nonalphanumeric'),
    ])