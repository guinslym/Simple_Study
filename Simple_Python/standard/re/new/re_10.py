#!/usr/bin/env python
# -*- coding:utf-8 -*-

from re_5 import test_pattern

test_pattern(
    'This is some text -- with punctuation.',
    [('[a-z]+','sequences of lowercase letters'),
     ('[A-Z]+','sequences of uppercase letters'),
     ('[a-zA-Z]+','sequences of lowercase or uppercase letters'),
     ('[A-Z][a-z]+','one uppercase followed by lowercase'),
    ])