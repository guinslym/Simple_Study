#!/usr/bin/env python
# -*- coding:utf-8 -*-

import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
print 'Dedented:'
print dedented_text