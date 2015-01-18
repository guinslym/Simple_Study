#!/usr/bin/env python
# -*- coding:utf-8 -*-

from re_5 import test_pattern

test_pattern(
    'abbaabbba',
    [('[ab]','either  a or b'),
     ('a[ab]+','a followed by 1 or  more a or b'),
     ('a[ab]+?','a followed by 1 or more a or b,not greedy'),
     ])