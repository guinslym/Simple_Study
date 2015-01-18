#!/usr/bin/env python
# -*- coding:utf-8 -*-

from re_5 import test_pattern

test_pattern(
    'This is some text -- with punctuation.',
    [(r'^\w+','word at start of string'),
    (r'\A\w+','word at start of string'),
    (r'\w+\S*$','word near end of string,skip punctuation'),
    (r'\w+\S*\Z','word near end of string,skip punctuation'),
    (r'\w*t\w*','word containing t'),
    (r'\bt\w+','t at start of word'),
    (r'\w+t\b','t at end of word'),
    (r'\Bt\B','t,not start or end of word')
    ])