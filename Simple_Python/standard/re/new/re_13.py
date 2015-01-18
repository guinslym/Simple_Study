#!/usr/bin/env python
# -*- coding:utf-8 -*-

from re_5 import test_pattern

test_pattern(
    r'\d+ \D+ \s+ ',
    [(r'\\.\+,','escape code'),
    ])