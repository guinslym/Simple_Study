#!/usr/bin/env python
# -*- coding:utf-8 -*-

from re_5 import test_pattern

test_pattern(
    'This is some text -- with punctuation.',
    [('[^-. ]+','sequences without -, ., or space'),]
    )